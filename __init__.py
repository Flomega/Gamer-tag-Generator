import random
import re

# List of forbidden characters
forbidden_characters = set("~&*@\\`^}]):,=$°|€äöüÖÄÜ")


def has_forbidden_characters(text):
    """
    Check if the input contains any forbidden characters.
    """
    return any(char in forbidden_characters for char in text)


def normalize_input(text):
    """
    Normalize the input by converting to lowercase, removing spaces, and replacing common character substitutions.
    Replace forbidden characters with a tilde (~), except for the letter 'a'.
    """
    # Define a mapping of forbidden characters to tilde (~)
    forbidden_to_tilde = {
        '~': '~', '&': '~', '*': '~', '@': '~', '\\': '~', '`': '~',
        '^': '~', '}': '~', ']': '~', ')': '~', ':': '~',
        ',': '~', '$': '~', '=': '~', '°': '~', '|': '~', '€': '~', 'ä': '~', 'ö': '~', 'ü': '~'
    }

    # Replace forbidden characters with their replacements
    for char, replacement in forbidden_to_tilde.items():
        text = text.replace(char, replacement)

    # Normalize the rest of the input
    text = text.lower().strip()  # Convert to lowercase and remove surrounding spaces
    text = re.sub(r'[0o]', 'o', text)  # Replace '0' with 'o'
    text = re.sub(r'[i1!l|]', 'i', text)  # Replace '1', '!', 'l', and '|' with 'i'
    text = re.sub(r'[7]', 't', text)  # Replace '7' with 't'
    text = re.sub(r'[s5]', 's', text)  # Replace '5' with 's'
    text = re.sub(r'[e3]', 'e', text)  # Replace '3' with 'e'
    # Remove all non-alphanumeric characters except underscores and replace them with tilde
    text = re.sub(r'[^a-zA-Z0-9]', '~', text)
    return text


def is_fortnite_variation(text):
    """
    Check if the normalized input matches any forbidden variations of 'Fortnite'.
    """
    # Forbidden patterns with only numbers and letters
    forbidden_patterns = set([
        "fortnite", "f0rtni7e", "f0rtni7t3", "fortnite", "f0rtnite", "f0rtni7e", "f0rtn!te", "f0rtn1gh7",
        "fortn!ght", "f0rtni7ght", "f0rtni7t3", "f0rtn!7e", "f0rtni7te",
        "f0rtni7t3", "f0rtni7ght", "fortn1te", "f0rtni7t3", "fortn1gh7",
        "f0rtni7ght", "fortni7t3", "f0rtni7t3", "fortn!ght", "f0rtn!ght",
        "fortmite", "vortmite", "f0rtmite", "f0rtm1te", "f0rtnite",
        "f0rtm!te", "fortm1te", "v0rtmite", "fortn1te", "v0rtni7e",
        "v0rtn!te", "v0rtn1gh7", "v0rtni7ght", "v0rtni7t3", "v0rtn!ght",
        "v0rtni7te", "v0rtni7t3", "v0rtni7ght", "v0rtni7t3", "v0rtni7ght",
        "v0rtni7t3", "v0rtni7ght", "v0rtn1gh7", "v0rtni7e", "v0rtni7t3",
        "v0rtn!ght", "v0rtni7t3", "v0rtni7t3", "v0rtni7ght", "v0rtni7e",
        "v0rtni7t3", "v0rtni7ght", "v0rtni7t3", "v0rtn1gh7", "v0rtni7t3",
        "v0rtni7t3", "v0rtni7ght", "v0rtni7t3", "v0rtn1gh7", "v0rtni7t3",
        "v0rtni7ght", "v0rtn1gh7", "v0rtni7t3", "v0rtni7ght", "v0rtni7e",
        "v0rtni7ght", "v0rtn1gh7", "v0rtni7e", "v0rtni7t3", "v0rtni7ght",
        "v0rtni7e", "v0rtni7t3", "v0rtn1gh7", "v0rtni7ght", "v0rtni7t3",
        "v0rtni7ght", "v0rtni7t3", "v0rtn1gh7", "v0rtni7ght", "v0rtn1gh7",
        "v0rtni7t3", "v0rtni7ght", "v0rtni7t3", "v0rtni7ght", "v0rtn1gh7",
        "v0rtni7t3", "v0rtni7ght", "v0rtn1gh7", "v0rtni7ght", "v0rtn1gh7",
        "v0rtni7t3", "v0rtni7ght", "v0rtni7ght", "v0rtni7e", "v0rtni7t3",
        "v0rtn1gh7", "v0rtni7t3", "v0rtni7ght", "v0rtni7t3", "v0rtni7ght",
        "v0rtn1gh7", "v0rtni7t3", "v0rtni7ght", "v0rtni7t3", "v0rtn1gh7",
        "v0rtni7t3", "v0rtni7ght", "v0rtn1gh7", "v0rtni7t3", "v0rtn1gh7",
        "v0rtni7ght", "v0rtni7t3", "v0rtni7ght", "v0rtni7e", "v0rtni7t3",
        "v0rtn1gh7", "v0rtni7t3", "v0rtni7ght", "v0rtni7t3", "v0rtni7ght",
        "v0rtn1gh7", "v0rtni7t3", "v0rtni7ght", "v0rtni7t3", "v0rtni7ght",
        "v0rtni7e", "v0rtni7ght", "v0rtn1gh7", "v0rtni7t3", "v0rtni7t3",
        "v0rtni7ght", "v0rtni7t3", "v0rtni7e", "v0rtni7t3", "v0rtni7ght",
        "v0rtni7t3", "v0rtni7t3", "v0rtni7ght", "v0rtni7t3", "v0rtn1gh7",
        "v0rtni7t3", "v0rtni7ght", "v0rtni7e", "v0rtn1gh7", "v0rtni7t3",
        "v0rtni7ght", "v0rtn1gh7", "v0rtni7t3", "v0rtni7ght", "v0rtn1gh7",
        "v0rtni7t3", "v0rtni7ght", "v0rtn1gh7", "v0rtni7t3", "v0rtni7ght",
        "v0rtn1gh7", "v0rtni7t3", "v0rtni7ght", "v0rtni7t3", "v0rtni7ght",
        "v0rtn1gh7", "v0rtni7t3", "v0rtni7ght", "v0rtn1gh7", "v0rtni7t3",
        "v0rtni7ght", "v0rtn1gh7", "v0rtni7t3", "v0rtni7ght", "v0rtni7ght",
        "v0rtni7t3", "v0rtni7ght", "v0rtni7t3", "v0rtn1gh7", "v0rtni7ght",
        "v0rtni7t3", "v0rtni7ght", "v0rtn1gh7", "v0rtni7t3", "v0rtni7ght",
        "v0rtni7t3", "v0rtni7ght", "v0rtn1gh7", "v0rtni7t3", "v0rtni7ght",
        "v0rtni7t3", "v0rtni7ght", "v0rtni7ght", "v0rtni7t3", "v0rtni7t3",
        "v0rtni7ght", "v0rtni7t3", "v0rtni7ght", "v0rtn1gh7", "v0rtni7t3",
        "v0rtni7ght", "v0rtn1gh7", "v0rtni7t3", "v0rtni7ght", "v0rtni7t3",
        "v0rtni7ght", "v0rtni7ght", "v0rtn1gh7", "v0rtni7t3", "v0rtni7t3",
        "v0rtn1gh7", "v0rtni7ght", "v0rtni7t3", "v0rtni7t3", "v0rtni7ght",
        "v0rtni7t3", "v0rtni7t3", "v0rtni7ght", "v0rtn1gh7", "v0rtni7t3",
        "v0rtni7ght", "v0rtni7t3", "v0rtn1gh7", "v0rtni7ght", "v0rtni7t3",
        "v0rtni7ght", "v0rtni7t3", "v0rtni7ght", "v0rtn1gh7", "v0rtni7t3",
        "v0rtni7ght", "v0rtn1gh7", "v0rtni7t3", "v0rtn1gh7", "v0rtni7ght",
        "v0rtni7t3", "v0rtn1gh7", "v0rtni7ght", "v0rtni7ght", "v0rtni7t3",
        "v0rtni7ght", "v0rtn1gh7", "v0rtni7t3", "v0rtni7ght", "v0rtn1gh7",
        "v0rtni7t3", "v0rtni7ght", "v0rtni7t3", "v0rtni7ght", "v0rtn1gh7",
        "v0rtni7t3", "v0rtni7ght", "v0rtn1gh7", "v0rtni7t3", "v0rtni7ght",
        "v0rtn1gh7", "v0rtni7t3", "v0rtn1gh7", "v0rtni7ght", "v0rtni7t3",
        "v0rtni7ght", "v0rtn1gh7", "v0rtni7t3", "v0rtn1gh7", "v0rtni7ght",
        "v0rtn1gh7", "v0rtni7t3", "v0rtni7ght", "v0rtni7t3", "v0rtni7ght",
        "v0rtn1gh7", "v0rtni7t3", "v0rtni7ght", "v0rtn1gh7", "v0rtni7t3",
        "v0rtni7ght", "v0rtn1gh7", "v0rtni7t3", "v0rtni7ght", "v0rtni7t3",
        "v0rtn1gh7", "v0rtni7ght", "v0rtni7t3", "v0rtni7t3", "v0rtn1gh7",
        "v0rtni7ght", "v0rtn1gh7", "v0rtni7t3", "v0rtni7ght", "v0rtni7ght",
        "v0rtni7t3", "v0rtn1gh7", "v0rtni7t3", "v0rtni7ght", "v0rtni7t3",
        "v0rtn1gh7", "v0rtni7t3", "v0rtni7ght", "v0rtn1gh7", "v0rtni7t3",
        "v0rtni7ght", "v0rtni7t3", "v0rtni7ght", "v0rtn1gh7", "v0rtni7t3",
        "v0rtn1gh7", "v0rtni7t3", "v0rtni7ght", "v0rtn1gh7", "v0rtni7t3",
        "v0rtni7ght", "v0rtn1gh7", "v0rtni7t3", "v0rtni7ght", "v0rtn1gh7",
        "v0rtni7t3", "v0rtn1gh7", "v0rtni7ght", "v0rtni7t3", "v0rtn1gh7",
        "v0rtni7t3", "v0rtni7ght", "v0rtn1gh7", "v0rtni7t3", "v0rtni7ght",
        "v0rtn1gh7", "v0rtni7t3", "v0rtni7ght", "v0rtni7t3", "v0rtn1gh7",
        "v0rtni7t3", "v0rtni7ght", "v0rtn1gh7", "v0rtni7t3", "v0rtni7ght",
        "v0rtni7t3", "v0rtn1gh7", "v0rtni7t3", "v0rtn1gh7", "v0rtni7ght",
        "v0rtn1gh7", "v0rtni7t3", "v0rtni7ght", "v0rtn1gh7", "v0rtni7t3",
        "v0rtni7ght", "v0rtn1gh7", "v0rtni7t3", "v0rtni7ght", "v0rtn1gh7",
        "v0rtni7t3", "v0rtni7ght", "v0rtni7t3", "v0rtn1gh7", "v0rtni7t3",
        "v0rtni7ght", "v0rtn1gh7", "v0rtni7t3", "v0rtni7ght", "v0rtn1gh7",
        "v0rtni7ght", "v0rtn1gh7", "v0rtni7t3", "v0rtn1gh7", "v0rtni7t3",
        "v0rtn1gh7", "v0rtni7ght", "v0rtn1gh7", "v0rtni7t3", "v0rtni7t3",
        "v0rtn1gh7", "v0rtni7ght", "v0rtn1gh7", "v0rtni7t3", "v0rtni7ght",
        "v0rtn1gh7", "v0rtni7t3", "v0rtn1gh7", "v0rtni7ght", "v0rtni7t3",
        "v0rtni7ght", "v0rtni7t3", "v0rtni7ght", "v0rtn1gh7", "v0rtni7t3",
        "v0rtni7ght", "v0rtn1gh7", "v0rtni7t3", "v0rtn1gh7", "v0rtni7ght",
        "v0rtni7t3", "v0rtni7ght", "v0rtni7t3", "v0rtn1gh7", "v0rtni7t3",
        "v0rtni7ght", "v0rtn1gh7", "v0rtni7t3", "v0rtni7ght", "v0rtn1gh7",
        "v0rtn1gh7", "v0rtni7t3", "v0rtni7ght", "v0rtni7t3", "v0rtn1gh7",
        "v0rtn1gh7", "v0rtni7ght", "v0rtni7t3", "v0rtni7ght", "v0rtn1gh7",
        "v0rtn1gh7", "v0rtni7t3", "v0rtn1gh7", "v0rtni7t3", "v0rtn1gh7",
        "v0rtn1gh7", "v0rtni7t3", "v0rtn1gh7", "v0rtni7ght", "v0rtn1gh7",
        "v0rtni7ght", "v0rtn1gh7", "v0rtn1gh7", "v0rtni7t3", "v0rtn1gh7",
        "v0rtni7ght", "v0rtni7ght", "v0rtni7t3", "v0rtni7ght", "v0rtn1gh7",
        "v0rtn1gh7", "v0rtni7ght", "v0rtn1gh7", "v0rtni7ght", "v0rtn1gh7",
        "v0rtni7ght", "v0rtni7t3", "v0rtn1gh7", "v0rtni7ght", "v0rtni7t3",
        "v0rtni7t3", "v0rtn1gh7", "v0rtni7ght", "v0rtni7t3", "v0rtni7ght",
        "v0rtni7t3", "v0rtn1gh7", "v0rtni7t3", "v0rtni7ght", "v0rtn1gh7",
        "v0rtn1gh7", "v0rtni7ght", "v0rtn1gh7", "v0rtni7ght", "v0rtni7t3",
        "v0rtni7ght", "v0rtn1gh7", "v0rtni7t3", "v0rtn1gh7", "v0rtni7t3",
        "v0rtni7ght", "v0rtn1gh7", "v0rtni7t3", "v0rtn1gh7", "v0rtni7t3",
        "v0rtni7ght", "v0rtni7t3", "v0rtn1gh7", "v0rtni7t3", "v0rtn1gh7",
        "v0rtni7ght", "v0rtni7t3", "v0rtn1gh7", "v0rtni7t3", "v0rtni7ght",
        "v0rtn1gh7", "v0rtni7t3", "v0rtn1gh7", "v0rtni7t3", "v0rtn1gh7",
        "v0rtn1gh7", "v0rtni7t3", "v0rtni7ght", "v0rtn1gh7", "v0rtni7t3",
        "v0rtni7ght", "v0rtn1gh7", "v0rtni7t3", "v0rtn1gh7", "v0rtni7ght",
        "v0rtn1gh7", "v0rtni7t3", "v0rtni7ght", "v0rtn1gh7", "v0rtn1gh7",
        "v0rtni7t3", "v0rtn1gh7", "v0rtni7t3", "v0rtn1gh7", "v0rtni7t3",
        "v0rtni7ght", "v0rtn1gh7", "v0rtni7t3", "v0rtni7ght", "v0rtn1gh7",
        "v0rtn1gh7", "v0rtni7t3", "v0rtn1gh7", "v0rtni7t3", "v0rtni7ght",
        "v0rtni7t3", "v0rtni7ght", "v0rtn1gh7", "v0rtni7t3", "v0rtn1gh7",
        "v0rtn1gh7", "v0rtni7t3", "v0rtni7t3", "v0rtni7ght", "v0rtni7ght",
        "v0rtni7ght", "v0rtn1gh7", "v0rtni7t3", "v0rtni7ght", "v0rtni7t3",
        "v0rtn1gh7", "v0rtni7ght", "v0rtni7ght", "v0rtn1gh7", "v0rtni7t3",
        "v0rtni7ght", "v0rtn1gh7", "v0rtni7t3", "v0rtni7ght", "v0rtni7ght",
        "v0rtn1gh7", "v0rtni7ght", "v0rtni7ght", "v0rtni7ght", "v0rtni7ght",
        "v0rtni7t3", "v0rtni7ght", "v0rtn1gh7", "v0rtn1gh7", "v0rtni7ght",
        "v0rtn1gh7", "v0rtni7ght", "v0rtni7t3", "v0rtn1gh7", "v0rtni7t3",
        "v0rtni7ght", "v0rtn1gh7", "v0rtni7t3", "v0rtn1gh7", "v0rtni7t3",
        "v0rtni7ght", "v0rtni7t3", "v0rtni7ght", "v0rtni7t3", "v0rtni7ght",
        "v0rtn1gh7", "v0rtni7t3", "v0rtni7ght", "v0rtni7t3", "v0rtn1gh7",
        "v0rtni7t3", "v0rtn1gh7", "v0rtni7t3", "v0rtn1gh7", "v0rtni7t3",
        "v0rtn1gh7", "v0rtni7t3", "v0rtni7ght", "v0rtni7t3", "v0rtni7ght",
        "v0rtn1gh7", "v0rtn1gh7", "v0rtni7ght", "v0rtni7t3", "v0rtn1gh7",
        "v0rtni7ght", "v0rtni7ght", "v0rtni7t3", "v0rtn1gh7", "v0rtni7ght",
        "v0rtni7ght", "v0rtn1gh7", "v0rtni7t3", "v0rtn1gh7", "v0rtni7ght",
        "v0rtn1gh7", "v0rtni7t3", "v0rtn1gh7", "v0rtni7t3", "v0rtni7ght",
        "v0rtn1gh7", "v0rtni7ght", "v0rtni7ght", "v0rtn1gh7", "v0rtn1gh7",
        "v0rtn1gh7", "v0rtni7t3", "v0rtni7ght", "v0rtni7t3", "v0rtni7ght",
        "v0rtni7ght", "v0rtn1gh7", "v0rtn1gh7", "v0rtni7ght", "v0rtn1gh7",
        "v0rtni7ght", "v0rtn1gh7", "v0rtni7ght", "v0rtni7t3", "v0rtn1gh7",
        "v0rtn1gh7", "v0rtni7t3", "v0rtn1gh7", "v0rtni7ght", "v0rtni7t3",
        "v0rtn1gh7", "v0rtn1gh7", "v0rtn1gh7", "v0rtni7t3", "v0rtn1gh7",
        "v0rtni7t3", "v0rtni7ght", "v0rtn1gh7", "v0rtni7t3", "v0rtni7ght",
        "v0rtn1gh7", "v0rtni7ght", "v0rtn1gh7", "v0rtn1gh7", "v0rtni7t3",
        "v0rtni7t3", "v0rtn1gh7", "v0rtni7ght", "v0rtn1gh7", "v0rtni7t3",
        "v0rtn1gh7", "v0rtni7t3", "v0rtni7ght", "v0rtni7ght", "v0rtni7t3",
        "v0rtn1gh7", "v0rtni7ght", "v0rtn1gh7", "v0rtni7t3", "v0rtn1gh7",
        "v0rtni7t3", "v0rtn1gh7", "v0rtn1gh7", "v0rtn1gh7", "v0rtni7t3",
        "v0rtni7ght", "v0rtni7t3", "v0rtni7ght", "v0rtni7t3", "v0rtn1gh7",
        "v0rtni7t3", "v0rtn1gh7", "v0rtn1gh7", "v0rtni7t3", "v0rtn1gh7",
        "v0rtni7ght", "v0rtn1gh7", "v0rtn1gh7", "v0rtni7t3", "v0rtni7ght",
        "v0rtni7t3", "v0rtn1gh7", "v0rtn1gh7", "v0rtni7ght", "v0rtn1gh7",
        "v0rtni7t3", "v0rtn1gh7", "v0rtn1gh7", "v0rtni7ght", "v0rtni7t3",
        "v0rtn1gh7", "v0rtn1gh7", "v0rtni7ght", "v0rtn1gh7", "v0rtni7t3",
        "v0rtn1gh7", "v0rtni7t3", "v0rtn1gh7", "v0rtn1gh7", "v0rtni7t3",
        "v0rtn1gh7", "v0rtni7t3", "v0rtni7ght", "v0rtn1gh7", "v0rtni7ght",
        "v0rtni7t3", "v0rtni7t3", "v0rtn1gh7", "v0rtni7ght", "v0rtn1gh7",
        "v0rtni7ght", "v0rtn1gh7", "v0rtni7t3", "v0rtn1gh7", "v0rtn1gh7",
        "v0rtni7ght", "v0rtn1gh7", "v0rtni7t3", "v0rtn1gh7", "v0rtni7t3",
        "v0rtni7t3", "v0rtni7ght", "v0rtn1gh7", "v0rtni7t3", "v0rtni7ght",
        "v0rtn1gh7", "v0rtni7ght", "v0rtni7ght", "v0rtni7t3", "v0rtni7ght",
        "v0rtn1gh7", "v0rtni7t3", "v0rtni7ght", "v0rtni7ght", "v0rtni7t3",
        "v0rtn1gh7", "v0rtni7ght", "v0rtni7ght", "v0rtni7t3", "v0rtni7ght",
        "v0rtn1gh7", "v0rtni7t3", "v0rtni7ght", "v0rtn1gh7", "v0rtn1gh7",
        "v0rtni7t3", "v0rtni7ght", "v0rtn1gh7", "v0rtni7ght", "v0rtn1gh7",
        "v0rtni7ght", "v0rtni7t3", "v0rtni7ght", "v0rtn1gh7", "v0rtni7t3",
        "v0rtni7t3", "v0rtni7ght", "v0rtn1gh7", "v0rtni7t3", "v0rtni7ght",
        "v0rtni7t3", "v0rtn1gh7", "v0rtni7ght", "v0rtn1gh7", "v0rtni7t3",
        "v0rtni7ght", "v0rtni7ght", "v0rtni7t3", "v0rtni7ght", "v0rtni7t3",
        "v0rtn1gh7", "v0rtn1gh7", "v0rtni7ght", "v0rtni7ght", "v0rtni7t3",
        "v0rtn1gh7", "v0rtni7t3", "v0rtni7t3", "v0rtn1gh7", "v0rtni7ght",
        "v0rtn1gh7", "v0rtni7t3", "v0rtn1gh7", "v0rtni7ght", "v0rtni7t3",
        "v0rtn1gh7", "v0rtni7ght", "v0rtni7ght", "v0rtni7t3", "v0rtn1gh7",
        "v0rtni7t3", "v0rtni7ght", "v0rtni7t3", "v0rtni7ght", "v0rtni7ght",
        "v0rtni7ght", "v0rtni7t3", "v0rtni7t3", "v0rtn1gh7", "v0rtni7t3",
        "v0rtni7ght", "v0rtn1gh7", "v0rtni7ght", "v0rtni7t3", "v0rtn1gh7",
        "v0rtni7t3", "v0rtn1gh7", "v0rtn1gh7", "v0rtni7t3", "v0rtni7ght",
        "v0rtni7t3", "v0rtn1gh7", "v0rtni7ght", "v0rtn1gh7", "v0rtni7t3",
        "v0rtni7ght", "v0rtn1gh7", "v0rtni7t3", "v0rtni7ght", "v0rtni7ght",
        "v0rtni7t3", "v0rtni7t3", "v0rtn1gh7", "v0rtni7t3", "v0rtn1gh7",
        "v0rtn1gh7", "v0rtni7ght", "v0rtni7t3", "v0rtn1gh7", "v0rtni7t3",
        "v0rtni7ght", "v0rtn1gh7", "v0rtni7t3", "v0rtni7t3", "v0rtni7ght",
        "v0rtni7t3", "v0rtn1gh7", "v0rtni7t3", "v0rtni7ght", "v0rtn1gh7",
        "v0rtni7t3", "v0rtni7t3", "v0rtn1gh7", "v0rtni7t3", "v0rtn1gh7",
        "v0rtn1gh7", "v0rtni7t3", "v0rtni7t3", "v0rtn1gh7", "v0rtni7ght",
        "v0rtn1gh7", "v0rtni7t3", "v0rtni7ght", "v0rtn1gh7", "v0rtni7ght",
        "v0rtni7t3", "v0rtni7t3", "v0rtn1gh7", "v0rtn1gh7", "v0rtni7t3",
        "v0rtn1gh7", "v0rtni7t3", "v0rtni7ght", "v0rtni7t3", "v0rtn1gh7",
        "v0rtn1gh7", "v0rtni7t3", "v0rtni7t3", "v0rtni7ght", "v0rtn1gh7",
        "v0rtni7ght", "v0rtni7ght", "v0rtn1gh7", "v0rtn1gh7", "v0rtni7t3",
        "v0rtni7t3", "v0rtn1gh7", "v0rtni7t3", "v0rtn1gh7", "v0rtni7t3",
        "v0rtn1gh7", "v0rtni7t3", "v0rtni7ght", "v0rtni7t3", "v0rtni7ght",
        "v0rtn1gh7", "v0rtni7t3", "v0rtni7t3", "v0rtn1gh7", "v0rtni7t3",
        "v0rtn1gh7", "v0rtni7t3", "v0rtn1gh7", "v0rtni7t3", "v0rtni7ght",
        "v0rtn1gh7", "v0rtni7t3", "v0rtn1gh7", "v0rtni7t3", "v0rtn1gh7",
        "v0rtn1gh7", "v0rtni7ght", "v0rtni7t3", "v0rtni7t3", "v0rtn1gh7",
        "v0rtni7t3", "v0rtn1gh7", "v0rtni7ght", "v0rtn1gh7", "v0rtni7t3",
        "v0rtni7t3", "v0rtn1gh7", "v0rtn1gh7", "v0rtni7ght", "v0rtni7t3",
        "v0rtni7t3", "v0rtni7ght", "v0rtn1gh7", "v0rtn1gh7", "v0rtni7t3",
        "v0rtni7ght", "v0rtni7t3", "v0rtn1gh7", "v0rtni7t3", "v0rtni7t3",
        "v0rtn1gh7", "v0rtni7t3", "v0rtni7ght", "v0rtn1gh7", "v0rtni7t3",
        "v0rtn1gh7", "v0rtni7t3", "v0rtn1gh7", "v0rtn1gh7", "v0rtn1gh7",
        "v0rtni7t3", "v0rtn1gh7", "v0rtni7t3", "v0rtni7t3", "v0rtni7ght",
        "v0rtni7t3", "v0rtni7ght", "v0rtn1gh7", "v0rtni7t3", "v0rtn1gh7",
        "v0rtni7t3", "v0rtn1gh7", "v0rtni7t3", "v0rtni7t3", "v0rtni7t3",
        "v0rtni7ght", "v0rtn1gh7", "v0rtni7t3", "v0rtni7ght", "v0rtn1gh7",
        "v0rtni7t3", "v0rtn1gh7", "v0rtn1gh7", "v0rtni7t3", "v0rtn1gh7",
        "v0rtni7t3", "v0rtni7ght", "v0rtn1gh7", "v0rtni7t3", "v0rtn1gh7",
        "v0rtni7t3", "v0rtni7t3", "v0rtni7ght", "v0rtn1gh7", "v0rtni7t3",
        "v0rtn1gh7", "v0rtni7t3", "v0rtn1gh7", "v0rtn1gh7", "v0rtni7ght",
        "v0rtn1gh7", "v0rtni7t3", "v0rtni7t3", "v0rtn1gh7", "v0rtni7t3",
        "v0rtn1gh7", "v0rtni7ght", "v0rtn1gh7", "v0rtn1gh7", "v0rtn1gh7",
        "v0rtni7ght", "v0rtn1gh7", "v0rtni7t3", "v0rtn1gh7", "v0rtni7t3",
        "v0rtn1gh7", "v0rtn1gh7", "v0rtni7t3", "v0rtn1gh7", "v0rtni7t3",
        "v0rtni7ght", "v0rtn1gh7", "v0rtn1gh7", "v0rtni7t3", "v0rtni7ght",
        "v0rtni7t3", "v0rtn1gh7", "v0rtni7t3", "v0rtni7ght", "v0rtni7t3",
        "v0rtn1gh7", "v0rtni7t3", "v0rtn1gh7", "v0rtn1gh7", "v0rtni7t3",
        "v0rtn1gh7", "v0rtni7ght", "v0rtni7t3", "v0rtn1gh7", "v0rtn1gh7",
        "v0rtni7t3", "v0rtn1gh7", "v0rtni7t3", "v0rtn1gh7", "v0rtni7ght",
        "v0rtn1gh7", "v0rtni7t3", "v0rtni7ght", "v0rtni7t3", "v0rtn1gh7",
        "v0rtni7ght", "v0rtn1gh7", "v0rtni7t3", "v0rtn1gh7", "v0rtn1gh7",
        "v0rtn1gh7", "v0rtni7ght", "v0rtn1gh7", "v0rtni7t3", "v0rtni7t3",
        "v0rtn1gh7", "v0rtn1gh7", "v0rtni7t3", "v0rtni7t3", "v0rtni7ght",
        "v0rtn1gh7", "v0rtn1gh7", "v0rtni7t3", "v0rtn1gh7", "v0rtn1gh7",
        "v0rtni7ght", "v0rtni7t3", "v0rtni7t3", "v0rtn1gh7", "v0rtni7ght",
        "v0rtn1gh7", "v0rtni7t3", "v0rtni7t3", "v0rtn1gh7", "v0rtni7ght",
        "v0rtn1gh7", "v0rtni7t3", "v0rtni7ght", "v0rtn1gh7", "v0rtni7t3",
        "v0rtn1gh7", "v0rtni7ght", "v0rtni7t3", "v0rtn1gh7", "v0rtn1gh7",
        "v0rtn1gh7", "v0rtni7ght", "v0rtni7t3", "v0rtn1gh7", "v0rtn1gh7",
        "v0rtn1gh7", "v0rtn1gh7", "v0rtn1gh7", "v0rtni7t3", "v0rtni7ght",
        "v0rtn1gh7", "v0rtni7t3", "v0rtni7t3", "v0rtn1gh7", "v0rtni7t3",
        "v0rtn1gh7", "v0rtni7ght", "v0rtn1gh7", "v0rtn1gh7", "v0rtni7ght",
        "v0rtni7t3", "v0rtn1gh7", "v0rtni7ght", "v0rtn1gh7", "v0rtn1gh7",
        "v0rtn1gh7", "v0rtn1gh7", "v0rtni7t3", "v0rtni7t3", "v0rtn1gh7",
        "v0rtni7ght", "v0rtn1gh7", "v0rtni7ght", "v0rtni7ght", "v0rtni7t3",
        "v0rtn1gh7", "v0rtni7t3", "v0rtn1gh7", "v0rtn1gh7", "v0rtn1gh7",
        "v0rtn1gh7", "v0rtni7ght", "v0rtn1gh7", "v0rtni7t3", "v0rtni7t3",
        "v0rtn1gh7", "v0rtni7t3", "v0rtni7t3", "v0rtni7ght", "v0rtn1gh7",
        "v0rtni7t3", "v0rtn1gh7", "v0rtni7ght", "v0rtn1gh7", "v0rtni7ght",
        "v0rtn1gh7", "v0rtni7t3", "v0rtni7ght", "v0rtn1gh7", "v0rtn1gh7",
        "v0rtn1gh7", "v0rtni7ght", "v0rtni7t3", "v0rtn1gh7", "v0rtn1gh7",
        "v0rtni7ght", "v0rtn1gh7", "v0rtni7ght", "v0rtni7ght", "v0rtn1gh7",
        "v0rtn1gh7", "v0rtni7t3", "v0rtni7t3", "v0rtni7t3", "v0rtn1gh7",
        "v0rtn1gh7", "v0rtn1gh7", "v0rtni7t3", "v0rtni7t3", "v0rtn1gh7",
        "v0rtni7t3", "v0rtni7ght", "v0rtn1gh7", "v0rtn1gh7", "v0rtn1gh7",
        "v0rtni7t3", "v0rtni7ght", "v0rtni7t3", "v0rtni7ght", "v0rtni7ght",
        "v0rtn1gh7", "v0rtn1gh7", "v0rtni7t3", "v0rtn1gh7", "v0rtni7t3",
        "v0rtni7ght", "v0rtni7t3", "v0rtni7ght", "v0rtn1gh7", "v0rtni7ght",
        "v0rtn1gh7", "v0rtn1gh7", "v0rtni7t3", "v0rtni7ght", "v0rtn1gh7",
        "v0rtni7t3", "v0rtni7ght", "v0rtn1gh7", "v0rtn1gh7", "v0rtn1gh7",
        "v0rtn1gh7", "v0rtni7t3", "v0rtn1gh7", "v0rtn1gh7", "v0rtn1gh7",
        "v0rtni7t3", "v0rtn1gh7", "v0rtn1gh7", "v0rtni7t3", "v0rtn1gh7",
        "v0rtn1gh7", "v0rtni7t3", "v0rtni7ght", "v0rtn1gh7", "v0rtni7t3",
        "v0rtn1gh7", "v0rtn1gh7", "v0rtn1gh7", "v0rtn1gh7", "v0rtni7t3",
        "v0rtni7t3", "v0rtni7t3", "v0rtn1gh7", "v0rtn1gh7", "v0rtni7t3",
        "v0rtn1gh7", "v0rtni7t3", "v0rtn1gh7", "v0rtni7ght", "v0rtn1gh7",
        "v0rtni7t3", "v0rtni7ght", "v0rtn1gh7", "v0rtni7t3", "v0rtni7t3",
        "v0rtn1gh7", "v0rtni7t3", "v0rtn1gh7", "v0rtni7ght", "v0rtn1gh7",
        "v0rtni7t3", "v0rtn1gh7", "v0rtni7t3", "v0rtn1gh7", "v0rtn1gh7",
        "v0rtn1gh7", "v0rtni7t3", "v0rtni7t3", "v0rtni7t3", "v0rtn1gh7",
        "v0rtni7ght", "v0rtn1gh7", "v0rtn1gh7", "v0rtni7ght", "v0rtn1gh7",
        "v0rtn1gh7", "v0rtni7t3", "v0rtn1gh7", "v0rtni7ght", "v0rtn1gh7",
        "v0rtn1gh7", "v0rtn1gh7", "v0rtn1gh7", "v0rtni7t3", "v0rtn1gh7",
        "v0rtn1gh7", "v0rtni7ght", "v0rtn1gh7", "v0rtn1gh7", "v0rtn1gh7",
        "v0rtni7ght", "v0rtn1gh7", "v0rtni7t3", "v0rtn1gh7", "v0rtn1gh7",
        "v0rtni7ght", "v0rtni7t3", "v0rtn1gh7", "v0rtni7ght", "v0rtn1gh7",
        "v0rtni7ght", "v0rtn1gh7", "v0rtni7t3", "v0rtn1gh7", "v0rtn1gh7",
        "v0rtn1gh7", "v0rtni7ght", "v0rtni7ght", "v0rtn1gh7", "v0rtn1gh7",
        "v0rtni7ght", "v0rtni7t3", "v0rtni7ght", "v0rtn1gh7", "v0rtn1gh7",
        "v0rtni7t3", "v0rtn1gh7", "v0rtn1gh7", "v0rtn1gh7", "v0rtni7t3",
        "v0rtni7ght", "v0rtn1gh7", "v0rtni7t3", "v0rtn1gh7", "v0rtn1gh7",
        "v0rtni7t3", "v0rtn1gh7", "v0rtni7t3", "v0rtn1gh7", "v0rtni7ght",
        "v0rtn1gh7", "v0rtni7t3", "v0rtn1gh7", "v0rtni7t3", "v0rtni7ght",
        "v0rtni7t3", "v0rtn1gh7", "v0rtn1gh7", "v0rtn1gh7", "v0rtni7t3",
        "v0rtn1gh7", "v0rtni7t3", "v0rtn1gh7", "v0rtn1gh7", "v0rtni7ght",
        "v0rtn1gh7", "v0rtni7t3", "v0rtn1gh7", "v0rtn1gh7", "v0rtni7t3",
        "v0rtn1gh7", "v0rtni7t3", "v0rtn1gh7", "v0rtni7ght", "v0rtn1gh7",
        "v0rtn1gh7", "v0rtni7ght", "v0rtni7t3", "v0rtni7t3", "v0rtn1gh7",
        "v0rtn1gh7", "v0rtn1gh7", "v0rtn1gh7", "v0rtn1gh7", "v0rtni7ght",
        "v0rtni7ght", "v0rtn1gh7", "v0rtni7t3", "v0rtn1gh7", "v0rtn1gh7",
        "v0rtni7ght", "v0rtn1gh7", "v0rtn1gh7", "v0rtn1gh7", "v0rtni7t3",
        "v0rtn1gh7", "v0rtn1gh7", "v0rtni7t3", "v0rtni7t3", "v0rtn1gh7",
        "v0rtni7t3", "v0rtni7ght", "v0rtn1gh7", "v0rtni7t3", "v0rtni7t3",
        "v0rtni7ght", "v0rtn1gh7", "v0rtn1gh7", "v0rtn1gh7", "v0rtni7t3",
        "v0rtni7t3", "v0rtni7t3", "v0rtn1gh7", "v0rtn1gh7", "v0rtni7t3",
        "v0rtni7t3", "v0rtn1gh7", "v0rtni7ght", "v0rtn1gh7", "v0rtn1gh7",
        "v0rtni7t3", "v0rtni7ght", "v0rtn1gh7", "v0rtn1gh7", "v0rtn1gh7",
        "v0rtn1gh7", "v0rtni7t3", "v0rtn1gh7", "v0rtni7t3", "v0rtni7ght",
        "v0rtn1gh7", "v0rtni7t3", "v0rtn1gh7", "v0rtni7t3", "v0rtn1gh7",
        "v0rtn1gh7", "v0rtni7ght", "v0rtn1gh7", "v0rtn1gh7", "v0rtni7ght",
        "v0rtn1gh7", "v0rtn1gh7", "v0rtni7t3", "v0rtn1gh7", "v0rtni7t3",
        "v0rtn1gh7", "v0rtn1gh7", "v0rtni7t3", "v0rtn1gh7", "v0rtn1gh7",
        "v0rtni7t3", "v0rtni7ght", "v0rtn1gh7", "v0rtni7t3", "v0rtn1gh7",
        "v0rtn1gh7", "v0rtni7ght", "v0rtn1gh7", "v0rtn1gh7", "v0rtn1gh7",
        "v0rtn1gh7", "v0rtni7t3", "v0rtni7ght", "v0rtn1gh7", "v0rtn1gh7",
        "v0rtni7t3", "v0rtn1gh7", "v0rtn1gh7", "v0rtni7ght", "v0rtni7t3",
        "v0rtn1gh7", "v0rtni7t3", "v0rtn1gh7", "v0rtni7ght", "v0rtni7t3",
        "v0rtn1gh7", "v0rtni7t3", "v0rtn1gh7", "v0rtni7ght", "v0rtn1gh7",
        "v0rtni7t3", "v0rtn1gh7", "v0rtn1gh7", "v0rtn1gh7", "v0rtni7t3",
        "v0rtn1gh7", "v0rtni7t3", "v0rtn1gh7", "v0rtn1gh7", "v0rtni7ght",
        "v0rtn1gh7", "v0rtni7t3", "v0rtni7t3", "v0rtn1gh7", "v0rtni7t3",
        "v0rtn1gh7", "v0rtn1gh7", "v0rtni7ght", "v0rtn1gh7", "v0rtni7t3",
        "v0rtni7ght", "v0rtni7ght", "v0rtn1gh7", "v0rtn1gh7", "v0rtni7t3",
        "v0rtn1gh7", "v0rtn1gh7", "v0rtn1gh7", "v0rtni7ght", "v0rtn1gh7",
        "v0rtni7t3", "v0rtn1gh7", "v0rtn1gh7", "v0rtni7t3", "v0rtni7t3",
        "v0rtn1gh7", "v0rtn1gh7", "v0rtni7t3", "v0rtn1gh7", "v0rtni7ght",
        "v0rtn1gh7", "v0rtni7t3", "v0rtni7ght", "v0rtn1gh7", "v0rtn1gh7",
        "v0rtni7t3", "v0rtni7ght", "v0rtn1gh7", "v0rtn1gh7", "v0rtn1gh7",
        "v0rtni7ght", "v0rtn1gh7", "v0rtni7ght", "v0rtn1gh7", "v0rtn1gh7",
        "v0rtni7ght", "v0rtni7ght", "v0rtni7t3", "v0rtn1gh7", "v0rtni7t3",
        "v0rtn1gh7", "v0rtni7t3", "v0rtn1gh7", "v0rtni7ght", "v0rtn1gh7",
        "v0rtn1gh7", "v0rtn1gh7", "v0rtni7t3", "v0rtni7ght", "v0rtn1gh7",
        "v0rtni7t3", "v0rtni7t3", "v0rtn1gh7", "v0rtn1gh7", "v0rtn1gh7",
        "v0rtni7ght", "v0rtni7t3", "v0rtni7t3", "v0rtn1gh7", "v0rtn1gh7",
        "v0rtni7t3", "v0rtn1gh7", "v0rtn1gh7", "v0rtn1gh7", "v0rtn1gh7",
        "v0rtni7t3", "v0rtni7t3", "v0rtni7t3", "v0rtni7t3", "v0rtn1gh7",
        "v0rtn1gh7", "v0rtn1gh7", "v0rtni7ght", "v0rtn1gh7", "v0rtni7t3",
        "v0rtn1gh7", "v0rtni7t3", "v0rtn1gh7", "v0rtni7t3", "v0rtn1gh7",
        "v0rtni7ght", "v0rtni7t3", "v0rtn1gh7", "v0rtni7t3", "v0rtni7ght",
        "v0rtn1gh7", "v0rtn1gh7", "v0rtn1gh7", "v0rtn1gh7", "v0rtn1gh7",
        "v0rtn1gh7", "v0rtn1gh7", "v0rtn1gh7", "v0rtn1gh7", "v0rtni7ght",
        "v0rtni7ght", "v0rtn1gh7", "v0rtni7ght", "v0rtn1gh7", "v0rtni7ght",
        "v0rtni7ght", "v0rtn1gh7", "v0rtn1gh7", "v0rtn1gh7", "v0rtni7ght",
        "v0rtn1gh7", "v0rtn1gh7", "v0rtni7t3", "v0rtni7ght", "v0rtn1gh7",
        "v0rtn1gh7", "v0rtni7t3", "v0rtni7ght", "v0rtn1gh7", "v0rtni7ght",
        "v0rtni7t3", "v0rtni7ght", "v0rtn1gh7", "v0rtni7t3", "v0rtn1gh7",
        "v0rtni7t3", "v0rtn1gh7", "v0rtni7t3", "v0rtni7ght", "v0rtn1gh7",
        "v0rtni7t3", "v0rtni7ght", "v0rtn1gh7", "v0rtn1gh7", "v0rtni7t3",
        "v0rtni7t3", "v0rtn1gh7", "v0rtn1gh7", "v0rtn1gh7", "v0rtni7ght",
        "v0rtni7t3", "v0rtn1gh7", "v0rtn1gh7", "v0rtn1gh7", "v0rtn1gh7",
        "v0rtni7t3", "v0rtn1gh7", "v0rtn1gh7", "v0rtni7ght", "v0rtn1gh7",
        "v0rtn1gh7", "v0rtn1gh7", "v0rtni7ght", "v0rtn1gh7", "v0rtni7ght",
        "v0rtn1gh7", "v0rtn1gh7", "v0rtni7t3", "v0rtni7ght", "v0rtn1gh7",
        "v0rtni7t3", "v0rtn1gh7", "v0rtn1gh7", "v0rtni7t3", "v0rtn1gh7",
        "v0rtni7ght", "v0rtni7ght", "v0rtn1gh7", "v0rtni7t3", "v0rtni7ght",
        "v0rtni7t3", "v0rtn1gh7", "v0rtni7ght", "v0rtn1gh7", "v0rtn1gh7",
        "v0rtn1gh7", "v0rtni7t3", "v0rtn1gh7", "v0rtn1gh7", "v0rtni7t3",
        "v0rtn1gh7", "v0rtn1gh7", "v0rtn1gh7", "v0rtni7ght", "v0rtn1gh7",
        "v0rtn1gh7", "v0rtn1gh7", "v0rtn1gh7", "v0rtn1gh7", "v0rtni7t3",
        "v0rtn1gh7", "v0rtni7t3", "v0rtn1gh7", "v0rtn1gh7", "v0rtn1gh7",
        "v0rtn1gh7", "v0rtni7t3", "v0rtn1gh7", "v0rtn1gh7", "v0rtn1gh7",
        "v0rtn1gh7", "v0rtni7t3", "v0rtni7ght", "v0rtn1gh7", "v0rtni7t3",
        "v0rtn1gh7", "v0rtn1gh7", "v0rtni7t3", "v0rtni7ght", "v0rtn1gh7",
        "v0rtni7ght", "v0rtn1gh7", "v0rtn1gh7", "v0rtn1gh7", "v0rtn1gh7",
        "v0rtn1gh7", "v0rtn1gh7", "v0rtn1gh7", "v0rtn1gh7", "v0rtn1gh7",
        "v0rtni7t3", "v0rtn1gh7", "v0rtn1gh7", "v0rtni7ght", "v0rtn1gh7",
        "v0rtn1gh7", "v0rtni7ght", "v0rtn1gh7", "v0rtni7t3", "v0rtn1gh7",
        "v0rtni7ght", "v0rtn1gh7", "v0rtn1gh7", "v0rtn1gh7", "v0rtn1gh7",
        "v0rtn1gh7", "v0rtni7t3", "v0rtn1gh7", "v0rtn1gh7", "v0rtn1gh7",
        "v0rtni7t3", "v0rtn1gh7", "v0rtni7ght", "v0rtni7ght", "v0rtn1gh7",
        "v0rtni7t3", "v0rtni7ght", "v0rtn1gh7", "v0rtni7t3", "v0rtn1gh7",
        "v0rtni7ght", "v0rtni7ght", "v0rtn1gh7", "v0rtni7ght", "v0rtn1gh7",
        "v0rtni7t3", "v0rtn1gh7", "v0rtni7ght", "v0rtni7ght", "v0rtni7ght",
        "v0rtn1gh7", "v0rtn1gh7", "v0rtn1gh7", "v0rtni7t3", "v0rtn1gh7",
        "v0rtn1gh7", "v0rtn1gh7", "v0rtni7t3", "v0rtni7t3", "v0rtn1gh7",
        "v0rtni7t3", "v0rtni7t3", "v0rtni7t3", "v0rtn1gh7", "v0rtn1gh7",
        "v0rtn1gh7", "v0rtni7t3", "v0rtn1gh7", "v0rtn1gh7", "v0rtni7t3",
        "v0rtn1gh7", "v0rtn1gh7", "v0rtni7ght", "v0rtni7t3", "v0rtn1gh7",
        "v0rtn1gh7", "v0rtn1gh7", "v0rtni7t3", "v0rtn1gh7", "v0rtn1gh7",
        "v0rtni7t3", "v0rtn1gh7", "v0rtn1gh7", "v0rtni7t3", "v0rtni7t3",
        "v0rtni7t3", "v0rtni7t3", "v0rtn1gh7", "v0rtn1gh7", "v0rtni7ght",
        "v0rtn1gh7", "v0rtni7t3", "v0rtn1gh7", "v0rtn1gh7", "v0rtni7ght",
        "v0rtni7t3", "v0rtn1gh7", "v0rtni7t3", "v0rtn1gh7", "v0rtn1gh7",
        "v0rtni7t3", "v0rtni7t3", "v0rtni7t3", "v0rtn1gh7", "v0rtni7t3",
        "v0rtn1gh7", "v0rtn1gh7", "v0rtni7t3", "v0rtni7t3", "v0rtn1gh7",
        "v0rtni7t3", "v0rtn1gh7", "v0rtn1gh7", "v0rtni7t3", "v0rtni7t3",
        "v0rtni7t3", "v0rtn1gh7", "v0rtn1gh7", "v0rtn1gh7", "v0rtni7t3",
        "v0rtni7t3", "v0rtn1gh7", "v0rtni7t3", "v0rtni7ght", "v0rtn1gh7",
        "v0rtn1gh7", "v0rtni7t3", "v0rtni7t3", "v0rtn1gh7", "v0rtni7t3",
        "v0rtn1gh7", "v0rtn1gh7", "v0rtn1gh7", "v0rtn1gh7", "v0rtni7t3",
        "v0rtn1gh7", "v0rtn1gh7", "v0rtni7t3", "v0rtni7t3", "v0rtn1gh7",
        "v0rtn1gh7", "v0rtni7t3", "v0rtn1gh7", "v0rtni7t3", "v0rtn1gh7",
        "v0rtni7t3", "v0rtn1gh7", "v0rtn1gh7", "v0rtn1gh7", "v0rtni7t3",
        "v0rtn1gh7", "v0rtn1gh7", "v0rtni7t3", "v0rtni7t3", "v0rtn1gh7",
        "v0rtni7t3", "v0rtni7t3", "v0rtni7t3", "v0rtn1gh7", "v0rtni7t3",
        "v0rtn1gh7", "v0rtn1gh7", "v0rtn1gh7", "v0rtn1gh7", "v0rtni7t3",
        "v0rtni7t3", "v0rtn1gh7", "v0rtn1gh7", "v0rtni7t3", "v0rtn1gh7",
        "v0rtni7t3", "v0rtni7t3", "v0rtn1gh7", "v0rtn1gh7", "v0rtn1gh7",
        "v0rtni7t3", "v0rtn1gh7", "v0rtn1gh7", "v0rtni7t3", "v0rtni7t3",
        "v0rtni7t3", "v0rtni7t3", "v0rtni7ght", "v0rtn1gh7", "v0rtn1gh7",
        "v0rtni7t3", "v0rtn1gh7", "v0rtn1gh7", "v0rtni7t3", "v0rtn1gh7",
        "v0rtn1gh7", "v0rtn1gh7", "v0rtn1gh7", "v0rtni7t3", "v0rtni7t3",
        "v0rtni7t3", "v0rtn1gh7", "v0rtni7t3", "v0rtn1gh7", "v0rtn1gh7",
        "v0rtn1gh7", "v0rtni7t3", "v0rtn1gh7", "v0rtni7t3", "v0rtn1gh7",
        "v0rtni7t3", "v0rtn1gh7", "v0rtn1gh7", "v0rtni7t3", "v0rtni7t3",
        "v0rtn1gh7", "v0rtni7t3", "v0rtn1gh7", "v0rtn1gh7", "v0rtni7t3",
        "v0rtni7t3", "v0rtni7t3", "v0rtni7t3", "v0rtn1gh7", "v0rtni7t3",
        "v0rtn1gh7", "v0rtn1gh7", "v0rtni7t3", "v0rtn1gh7", "v0rtn1gh7",
        "v0rtni7t3", "v0rtn1gh7", "v0rtni7t3", "v0rtn1gh7", "v0rtni7t3",
        "v0rtni7t3", "v0rtn1gh7", "v0rtn1gh7", "v0rtni7t3", "v0rtni7t3",
        "v0rtni7t3", "v0rtn1gh7", "v0rtn1gh7", "v0rtn1gh7", "v0rtni7t3",
        "v0rtni7t3", "v0rtn1gh7", "v0rtn1gh7", "v0rtni7t3", "v0rtn1gh7",
        "v0rtni7t3", "v0rtn1gh7", "v0rtni7t3", "v0rtn1gh7", "v0rtni7t3",
        "v0rtn1gh7", "v0rtn1gh7", "v0rtni7t3", "v0rtni7t3", "v0rtni7t3",
        "v0rtni7t3", "v0rtn1gh7", "v0rtni7t3", "v0rtn1gh7", "v0rtn1gh7",
        "v0rtn1gh7", "v0rtni7t3", "v0rtni7t3", "v0rtni7t3", "v0rtni7t3",
        "v0rtn1gh7", "v0rtn1gh7", "v0rtni7t3", "v0rtn1gh7", "v0rtn1gh7",
        "v0rtn1gh7", "v0rtn1gh7", "v0rtn1gh7", "v0rtn1gh7", "v0rtni7t3",
        "v0rtni7t3", "v0rtni7t3", "v0rtni7t3", "v0rtn1gh7", "v0rtn1gh7",
        "v0rtn1gh7", "v0rtni7t3", "v0rtni7t3", "v0rtn1gh7", "v0rtni7t3",
        "v0rtn1gh7", "v0rtn1gh7", "v0rtn1gh7", "v0rtni7t3", "v0rtn1gh7",
        "v0rtn1gh7", "v0rtn1gh7", "v0rtni7t3", "v0rtni7t3", "v0rtn1gh7",
        "v0rtn1gh7", "v0rtn1gh7", "v0rtn1gh7", "v0rtni7t3", "v0rtni7t3",
        "v0rtni7t3", "v0rtn1gh7", "v0rtni7t3", "v0rtn1gh7", "v0rtn1gh7",
        "v0rtni7t3", "v0rtn1gh7", "v0rtn1gh7", "v0rtni7t3", "v0rtni7t3",
        "v0rtn1gh7", "v0rtni7t3", "v0rtni7t3", "v0rtni7t3", "v0rtn1gh7",
        "v0rtni7t3", "v0rtn1gh7", "v0rtn1gh7", "v0rtni7t3", "v0rtn1gh7",
        "v0rtn1gh7", "v0rtni7t3", "v0rtn1gh7", "v0rtn1gh7", "v0rtni7t3",
        "v0rtn1gh7", "v0rtn1gh7", "v0rtni7t3", "v0rtni7t3", "v0rtn1gh7",
        "v0rtni7t3", "v0rtni7t3", "v0rtn1gh7", "v0rtni7t3", "v0rtni7t3",
        "v0rtn1gh7", "v0rtn1gh7", "v0rtni7t3", "v0rtn1gh7", "v0rtn1gh7",
        "v0rtni7t3", "v0rtn1gh7", "v0rtni7t3", "v0rtn1gh7", "v0rtn1gh7",
        "v0rtn1gh7", "v0rtni7t3", "v0rtni7t3", "v0rtni7t3", "v0rtn1gh7",
        "v0rtn1gh7", "v0rtn1gh7", "v0rtni7t3", "v0rtn1gh7", "v0rtn1gh7",
        "v0rtni7t3", "v0rtni7t3", "v0rtn1gh7", "v0rtni7t3", "v0rtn1gh7",
        "v0rtni7t3", "v0rtn1gh7", "v0rtni7t3", "v0rtn1gh7", "v0rtn1gh7",
        "v0rtni7t3", "v0rtn1gh7", "v0rtn1gh7", "v0rtn1gh7", "v0rtn1gh7",
        "v0rtni7t3", "v0rtn1gh7", "v0rtni7t3", "v0rtni7t3", "v0rtn1gh7",
        "v0rtn1gh7", "v0rtni7t3", "v0rtn1gh7", "v0rtn1gh7", "v0rtni7t3",
        "v0rtn1gh7", "v0rtni7t3", "v0rtn1gh7", "v0rtn1gh7", "v0rtni7t3",
    ])

    normalized_text = normalize_input(text)

    # Check if the normalized text matches any forbidden patterns
    return normalized_text in forbidden_patterns


def generate_gamer_tag():
    print("~~~~~Welcome to the gamer tag name generator!~~~~~")

    # Ask the user what game they need the username for
    while True:
        game = input("What game do you need this username for? ").strip()
        if has_forbidden_characters(game):
            print("Not allowed: Illegal character found.")
            continue
        # Normalize and check for invalid characters
        normalized_game = normalize_input(game)
        if not re.match(r'^[a-zA-Z0-9~]*$', normalized_game):
            print("Invalid input. Please use only letters and numbers.")
        elif is_fortnite_variation(normalized_game):
            print("Sorry, 'Fortnite' and its variations are not allowed. Please choose another game.")
        else:
            break

    # Define possible questions and associated responses
    questions = [
        ("What is your favorite game?", "game"),
        ("What's your favorite weapon in a game?", "weapon"),
        ("Who is your favorite gaming character?", "character"),
        ("What's your favorite map or level in a game?", "map_name"),
        ("What's your favorite game genre (e.g., FPS, RPG, MOBA)?", "genre")
    ]

    # Randomly select a question
    selected_question, response_key = random.choice(questions)

    while True:
        # Ask the selected question
        response = input(selected_question + " ").strip()
        if has_forbidden_characters(response):
            print("Not allowed: Illegal character found.")
            continue
        # Normalize and check for invalid characters
        normalized_response = normalize_input(response)
        if not re.match(r'^[a-zA-Z0-9~]*$', normalized_response):
            print("Invalid input. Please use only letters and numbers.")
        elif is_fortnite_variation(normalized_response):
            print("Sorry, 'Fortnite' and its variations are not allowed. Please provide a different response.")
        else:
            break

    # Replace spaces with underscores in the user's response
    response = response.replace(" ", "_")

    # Choose a random number
    rand_number = random.randint(1, 100)

    # Choose a random character to add at the end
    random_char = random.choice(['#', '_', '-'])

    # Combine the response, random number, and random character to generate the gamer tag
    gamer_tag = response + str(rand_number) + random_char

    # Display the generated gamer tag
    print("Your gamer tag should be: " + gamer_tag + " (and if that name doesn't work, it's not my problem, womp womp)")


# Main loop to allow restarting
while True:
    generate_gamer_tag()
    restart = input("Do you want to generate another gamer tag? (yes/no) ").strip().lower()
    if restart != 'yes':
        break
