"""
COMMANDS/files.py
-----------------
NOVA file and folder controls.
"""

import os


class FileManager:

    # =================================
    # COMMON WINDOWS FOLDERS
    # =================================

    def get_folder(self, name: str):

        folders = {
            "desktop": os.path.join(
                os.path.expanduser("~"),
                "Desktop"
            ),

            "downloads": os.path.join(
                os.path.expanduser("~"),
                "Downloads"
            ),

            "documents": os.path.join(
                os.path.expanduser("~"),
                "Documents"
            ),

            "pictures": os.path.join(
                os.path.expanduser("~"),
                "Pictures"
            ),

            "videos": os.path.join(
                os.path.expanduser("~"),
                "Videos"
            ),

            "music": os.path.join(
                os.path.expanduser("~"),
                "Music"
            ),
        }

        return folders.get(
            name.lower().strip()
        )

    # =================================
    # OPEN COMMON FOLDER
    # =================================

    def open_folder(self, name: str):

        path = self.get_folder(name)

        if not path:
            return False

        if not os.path.exists(path):
            return f"I couldn't find your {name} folder."

        try:
            os.startfile(path)
            return True

        except Exception as e:
            print("File Error:", e)
            return False

    # =================================
    # CREATE FOLDER
    # =================================

    def create_folder(self, name: str):

        name = name.strip()

        if not name:
            return False

        desktop = self.get_folder("desktop")

        if not desktop:
            return False

        path = os.path.join(
            desktop,
            name
        )

        try:
            os.makedirs(
                path,
                exist_ok=True
            )

            return True

        except Exception as e:
            print("File Error:", e)
            return False

    # =================================
    # FILE TYPE ALIASES
    # =================================

    def get_extension(self, file_type: str):

        extensions = {
            "pdf": ".pdf",
            "pdfs": ".pdf",

            "png": ".png",
            "pngs": ".png",

            "jpg": ".jpg",
            "jpgs": ".jpg",

            "jpeg": ".jpeg",
            "jpegs": ".jpeg",

            "gif": ".gif",
            "gifs": ".gif",

            "webp": ".webp",

            "python": ".py",
            "python file": ".py",
            "python files": ".py",
            "py": ".py",

            "text": ".txt",
            "text file": ".txt",
            "text files": ".txt",
            "txt": ".txt",

            "word": ".docx",
            "word file": ".docx",
            "word files": ".docx",
            "docx": ".docx",

            "excel": ".xlsx",
            "excel file": ".xlsx",
            "excel files": ".xlsx",
            "xlsx": ".xlsx",

            "powerpoint": ".pptx",
            "powerpoint file": ".pptx",
            "powerpoint files": ".pptx",
            "pptx": ".pptx",

            "zip": ".zip",
            "zips": ".zip",

            "rar": ".rar",
            "rars": ".rar",
        }

        return extensions.get(
            file_type.lower().strip()
        )

    # =================================
    # SEARCH FILES & FOLDERS
    # =================================

    def search(
        self,
        query: str = "",
        extension=None,
        folders_only=False
    ):

        query = query.lower().strip()

        # ---------------------------------
        # NORMALIZE EXTENSION
        # ---------------------------------

        if extension:

            extension = extension.lower().strip()

            if not extension.startswith("."):
                extension = "." + extension

        # ---------------------------------
        # REMOVE SEARCH INSTRUCTION WORDS
        # ---------------------------------

        removable_words = [
            "folder",
            "folders",
            "file",
            "files",
            "directory",
            "directories"
        ]

        for word in removable_words:

            query = query.replace(
                f" {word}",
                ""
            )

            query = query.replace(
                f"{word} ",
                ""
            )

        query = query.strip()

        # ---------------------------------
        # SEARCH LOCATIONS
        # ---------------------------------

        search_locations = [
            self.get_folder("desktop"),
            self.get_folder("downloads"),
            self.get_folder("documents"),
            self.get_folder("pictures"),
            self.get_folder("videos"),
            self.get_folder("music"),
        ]

        results = []

        # ---------------------------------
        # SEARCH EACH LOCATION
        # ---------------------------------

        for location in search_locations:

            if not location:
                continue

            if not os.path.exists(location):
                continue

            try:

                for root, dirs, file_names in os.walk(
                    location
                ):

                    # =================================
                    # FOLDER SEARCH
                    # =================================

                    if not extension:

                        for folder_name in dirs:

                            folder_lower = (
                                folder_name.lower()
                            )

                            if (
                                not query
                                or query in folder_lower
                            ):

                                path = os.path.join(
                                    root,
                                    folder_name
                                )

                                if path not in results:

                                    results.append(path)

                    # =================================
                    # FILE SEARCH
                    # =================================

                    if not folders_only:

                        for file_name in file_names:

                            filename_lower = (
                                file_name.lower()
                            )

                            # Extension filter
                            if extension:

                                if not filename_lower.endswith(
                                    extension
                                ):
                                    continue

                            # Name filter
                            if query:

                                if query not in filename_lower:
                                    continue

                            path = os.path.join(
                                root,
                                file_name
                            )

                            if path not in results:

                                results.append(path)

                    # =================================
                    # SAFETY LIMIT
                    # =================================

                    if len(results) >= 50:

                        return results[:50]

            except PermissionError:

                continue

            except OSError as e:

                print(
                    "Search Error:",
                    e
                )

                continue

        return results

    # =================================
    # SMART MATCHING
    # =================================

    def find_best_match(
        self,
        query: str,
        results: list
    ):

        if not results:
            return None

        query = query.lower().strip()

        # Remove common words
        removable_words = [
            "folder",
            "folders",
            "file",
            "files",
            "the",
            "my"
        ]

        query_words = query.split()

        query_words = [
            word
            for word in query_words
            if word not in removable_words
        ]

        clean_query = " ".join(
            query_words
        ).strip()

        if not clean_query:
            clean_query = query

        # ---------------------------------
        # SCORE RESULTS
        # ---------------------------------

        scored_results = []

        for path in results:

            filename = os.path.basename(
                path
            )

            name_without_extension = (
                os.path.splitext(filename)[0]
            )

            filename_lower = (
                filename.lower()
            )

            name_lower = (
                name_without_extension.lower()
            )

            score = 0

            # Exact filename
            if filename_lower == clean_query:
                score += 1000

            # Exact name without extension
            if name_lower == clean_query:
                score += 900

            # Starts with query
            if name_lower.startswith(
                clean_query
            ):
                score += 500

            # Contains complete query
            if clean_query in name_lower:
                score += 300

            # Individual words
            for word in clean_query.split():

                if word in name_lower:
                    score += 50

            # Slight preference for shorter names
            score -= len(name_lower)

            scored_results.append(
                (
                    score,
                    path
                )
            )

        # ---------------------------------
        # SORT
        # ---------------------------------

        scored_results.sort(
            key=lambda item: item[0],
            reverse=True
        )

        best_score = (
            scored_results[0][0]
        )

        best_matches = [
            path
            for score, path
            in scored_results
            if score == best_score
        ]

        # ---------------------------------
        # ONE CLEAR BEST MATCH
        # ---------------------------------

        if len(best_matches) == 1:

            return {
                "status": "best",
                "path": best_matches[0],
                "matches": best_matches
            }

        # ---------------------------------
        # MULTIPLE EQUAL MATCHES
        # ---------------------------------

        return {
            "status": "multiple",
            "path": None,
            "matches": best_matches
        }

    # =================================
    # OPEN FILE OR FOLDER
    # =================================

    def open_path(self, path: str):

        if not path:
            return False

        if not os.path.exists(path):
            return False

        try:

            os.startfile(path)

            return True

        except Exception as e:

            print(
                "Open File Error:",
                e
            )

            return False


# =====================================
# CREATE FILE MANAGER
# =====================================

files = FileManager()