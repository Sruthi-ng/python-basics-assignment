{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyPUkbytX0TW4C0RxVNxWjnm",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/Sruthi-ng/python-basics-assignment/blob/main/python_basics_Sruthi_Nagari_Gurumoorthy.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 6,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "DM5vZ2TnIdfC",
        "outputId": "dfa530f6-1f3f-49ab-ff9f-9c9294c8d57f"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Alpha 87 6.1 True\n",
            "Name: Alpha | Age: 87 | Height: 6.1 | Student: True\n",
            "age_in_months is: 1044 \n",
            " age_in_days is: 31755 \n",
            " age_remainder is: 3 \n",
            " age_power_of_2 is: 7569\n"
          ]
        }
      ],
      "source": [
        "# Task 1\n",
        "name=\"Alpha\"\n",
        "age = 87\n",
        "height = 6.1\n",
        "is_student = True\n",
        "print (name, age, height, is_student)\n",
        "\n",
        "\n",
        "# Task 2: String Formatting Using the variables from Task 1, print a sentence in the following format: Name: <name> | Age: <age> | Height: <height> | Student: <is_student>\n",
        "print(f\"Name: {name} | Age: {age} | Height: {height} | Student: {is_student}\")\n",
        "\n",
        "# Task 3: Arithmetic Operations Using the age variable, calculate and print:Age in months, Age in days (assume 365 days/year), The remainder when age is divided by 7, Age raised to the power of 2\n",
        "age_in_months = age * 12\n",
        "age_in_days = age * 365\n",
        "age_remainder = age % 7\n",
        "age_power_of_2 = age ** 2\n",
        "print (\"age_in_months is:\", age*12 ,  \"\\n age_in_days is:\", age * 365, \"\\n age_remainder is:\", age % 7, \"\\n age_power_of_2 is:\", age ** 2)\n",
        "\n"
      ]
    }
  ]
}