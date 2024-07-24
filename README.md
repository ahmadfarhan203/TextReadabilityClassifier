# TextReadabilityClassifier
Determining the readability level of a text (elementary school, high school, university, technical document)

# Project Title: Determining the Readability Levels of Texts

# Objective and Goals:

The purpose of this project is to determine the readability level of given texts and evaluate whether these texts are suitable for the target audience. In this regard, we will use the Flesch-Kincaid readability test to determine whether the texts are at the level of elementary school, middle school, high school, university, or technical document.

# Scope and Limitations:

The project will analyze texts written in Turkish. The CMU Pronouncing Dictionary (CMUDict) will be used to determine the number of syllables, and an alternative syllable estimation method will be applied for words not found in the dictionary. This project will be especially useful for determining the readability level of educational materials, technical documents, and various written contents.

# Problem Definition

# Problem Description:

Readability level is an important measure that determines how easily a text can be understood. This level is crucial for creating content suitable for the target audience. Accurate determination of the readability level is necessary for educational materials, technical documents, and various media contents.

# Motivation:

Determining the correct readability level enhances the effectiveness of educational materials, official documents, and other written content. This allows readers to better understand the text and benefit more efficiently from the information. Additionally, making educational materials suitable for the target audience supports the learning process and facilitates knowledge acquisition.

# Input and Output

    Input: A sample text:
    An example text will be here. We will determine the readability level of the text.

    Output: Readability level and Flesch-Kincaid grade level:
    Text: An example text will be here. We will determine the readability level of the text.
    Readability Level: Elementary School (Flesch-Kincaid Grade Level: 3.67)

# Method and Steps

This solution has been implemented using the Flesch-Kincaid readability test. The Flesch-Kincaid test determines the readability of a text by using the number of words per sentence and the number of syllables per word.

# Steps:

    # Splitting the Text:
        The text is divided into sentences.
        Sentences are divided into words.

    # Calculating the Number of Syllables:
        The number of syllables in each word is calculated.

    # Applying the Formula:
        The readability level is calculated using the Flesch-Kincaid readability formula.
        ![image](https://github.com/user-attachments/assets/72165ce0-b642-49f0-a4cc-95af81b8e6de)


    # Determining the Level:
        The level of the text is determined based on the calculated readability grade (elementary school, middle school, high school, university, technical document).

# Originality of the Solution

This solution uses the CMU Pronouncing Dictionary (CMUDict) from the nltk library to accurately determine the number of syllables per word. Additionally, a method of counting vowels is used as an alternative when the syllable count cannot be predicted. This ensures an accurate determination of the text's readability level.

# Similar Solutions and Resources:

    # Similar Solutions:
        The Flesch-Kincaid readability test is widely used and available in many text editors and educational software.
        Other readability tests such as the Gunning Fog Index and the SMOG Index can also be used for text analysis.

    # Resources:
        nltk Library: https://www.nltk.org/
        CMU Pronouncing Dictionary (CMUDict): http://www.speech.cs.cmu.edu/cgi-bin/cmudict
        Flesch-Kincaid Readability Test: https://en.wikipedia.org/wiki/Flesch%E2%80%93Kincaid_readability_tests
