# Файл lang.py
# Содержит словарь и функцию, которая определяет язык в файлах



LANGUAGES = {

    "c": "C",
    "cpp": "C++",
    "cc": "C++",
    "cxx": "C++",
    "h": "Заголовочный файл C/C++",
    "hpp": "Заголовочный файл C/C++",
    "cs": "C#",
    "go": "Go",
    "rs": "Rust",
    "swift": "Swift",
    "m": "Objective-C",
    "mm": "Objective-C++",
    "asm": "Ассемблер",
    "s": "Ассемблер",

    "java": "Java",
    "kt": "Kotlin",
    "kts": "Kotlin Script",
    "groovy": "Groovy",
    "scala": "Scala",

    "py": "Python",
    "pyw": "Python (GUI)",
    "rb": "Ruby",
    "pl": "Perl",
    "pm": "Perl Module",
    "php": "PHP",
    "phtml": "PHP HTML",

    "js": "JavaScript",
    "jsx": "React JSX",
    "ts": "TypeScript",
    "tsx": "React TSX",
    "dart": "Dart",
    "vue": "Vue Component",
    "html": "HTML",
    "htm": "HTML",
    "css": "CSS",
    "scss": "Sass SCSS",
    "sass": "Sass",
    "less": "Less",

    "sql": "SQL",
    "psql": "PostgreSQL SQL",
    "nosql": "NoSQL Query",

    "json": "JSON",
    "jsonc": "JSON with Comments",
    "yaml": "YAML",
    "yml": "YAML",
    "xml": "XML",
    "toml": "TOML",
    "ini": "INI Config",
    "conf": "Configuration File",
    "md": "Markdown",
    "tex": "LaTeX",

    "sh": "Bash/Sh Script",
    "bash": "Bash Script",
    "zsh": "Zsh Script",
    "bat": "Windows Batch",
    "cmd": "Windows Command",
    "ps1": "PowerShell",
    "vbs": "VBScript",

    "r": "R",
    "lua": "Lua",
    "ex": "Elixir",
    "exs": "Elixir Script",
    "erl": "Erlang",
    "hrl": "Erlang Header",
    "hs": "Haskell",
    "clj": "Clojure",
    "fs": "F#",
    "ml": "OCaml",
    "nim": "Nim",
    "zig": "Zig",
    "pas": "Pascal",
    "d": "D",
    "v": "V",
}

def detect_language(ext):
    return LANGUAGES.get(ext, "Неизвестный тип файла")
