# Imports.
import sys
import os
import shutil


def is_fruit_article(article: str) -> bool:
    return "fruit" in article


def is_university_article(article: str) -> bool:
    return "<title>Universit" in article or "University - Wikipedia" in article


def get_article_class(article: str) -> str:
    # Use the functions from above to determine the class.
    if is_fruit_article(article):
        return "fruits"
    elif is_university_article(article):
        return "schools"
    else:
        return "brands"


def get_article_name(article: str) -> str:
    # Get the title of the article.
    start_index = article.index("<title>") + len("<title>")
    end_index = article.index("</title>")
    article_title = article[start_index:end_index]

    # Get the actual name being referred to.
    wikipedia_index = article_title.index(" - Wikipedia")
    return article_title[:wikipedia_index]


def process_article(path_to_article: str):
    # Read the article.
    with open(path_to_article) as article_file:
        article = article_file.read()

    # Determine where we want to move the article to.
    article_class = get_article_class(article)
    article_name = get_article_name(article)
    article_destination = os.path.join(
        "organized",
        article_class,
        article_name + ".html",
    )

    # Move the article.
    shutil.copy(path_to_article, article_destination)


# EXTRA: Make this script work by double clicking.
# You can ignore this line (unless you're curious how it works!).
os.chdir(os.path.join(os.path.dirname(os.path.realpath(__file__)), ".."))

# Check where to load the data from.
if len(sys.argv) >= 2:
    # The user passed in at least one argument (argv[0] is the program name).
    data_load_location = sys.argv[1]
else:
    # Use the default data location.
    data_load_location = "data/"

# Remove any work from previous runs.
shutil.rmtree("organized", ignore_errors=True)

# Create all the output directories.
for directory_name in ["fruits", "schools", "brands"]:
    directory_path = os.path.join("organized", directory_name)
    os.makedirs(directory_path)

# Loop over all the data files and process each article.
for current_dir, directories, files in os.walk(data_load_location):
    for file_path in files:
        path_to_article = os.path.join(current_dir, file_path)
        process_article(path_to_article)
