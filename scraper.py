import requests
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup

def main():
    url = "https://news.ycombinator.com/item?id=42919502"
    response = requests.get(url)

    soup = BeautifulSoup(response.content, "html.parser")
    # find all elements with class="ind" and indent level = 0
    elements = soup.find_all(class_="ind")

    # for each of these elements, find the next element that contains comments
    comments = [e.find_next(class_="comment") for e in elements if e.find_next(class_="comment")]

    # Map of technologies keyword to search for and the occurrence initialized at 0
    keywords = {"python": 0, "javascript": 0, "typescript": 0, "go": 0, "c#": 0, "java": 0, "rust": 0 }

    # Loop through each comment and analyze the text
    for comment in comments:
        # get the comment text and lower case it
        comment_text = comment.get_text().lower()

        # split comment by space which create an array of words
        words = comment_text.split(" ")

        # Clean up the words by stripping punctuation
        words = {w.strip(".,/:;!@") for w in words}

        # Check for the presence of each keyword in the words set
        for k in keywords:
            if k in words:
                keywords[k] += 1  # Increment keyword count

    print(keywords)  # Print the keyword frequencies

    # Plot a bar graph inside the main function
    plt.bar(keywords.keys(), keywords.values())
    # Add labels
    plt.xlabel("Language")
    plt.ylabel("# of Mentions")
    plt.title("Keyword Frequency in Comments")
    plt.show()

if __name__ == "__main__":
    main()
