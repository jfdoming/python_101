# Imports.
import os
import shutil


def is_fruit_article(article: str) -> bool:
    return "fruit" in article


def is_university_article(article: str) -> bool:
    return "<title>Universit" in article or "University - Wikipedia" in article


def get_article_class(article: str) -> str:
    # Use the functions from above to determine the class.
    if is_fruit_article(article):
        return "fruit"
    elif is_university_article(article):
        return "university"
    else:
        return "brand"


def get_article_name(article: str) -> str:
    # Get the title of the article.
    start_index = article.index("<title>") + len("<title>")
    end_index = article.index("</title>")
    article_title = article[start_index:end_index]

    # Get the actual name being referred to.
    wikipedia_index = article_title.index(" - Wikipedia")
    return article_title[0:wikipedia_index]


def process_article(path_to_article: str):
    # Read the article.
    with open(path_to_article) as f:
        article_body = f.read()

    # Determine where we want to move the article to.
    article_name = get_article_name(article_body)
    article_class = get_article_class(article_body)
    article_destination = os.path.join("organized", article_class, article_name + ".html")

    # Move the article.
    shutil.copy(path_to_article, article_destination)


# Check where to load the data from.
load_location = "data/"

# Remove any work from previous runs.
shutil.rmtree("organized/", ignore_errors=True)

# Create all the output directories.
os.makedirs("organized")
os.makedirs("organized/fruit")
os.makedirs("organized/university")
os.makedirs("organized/brand")

# Loop over all the data files and process each article.
for root, dirs, files in os.walk(load_location):
    for filename in files:
        path = os.path.join(root, filename)
        process_article(path)
