{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "a9b72253-1a9a-41ae-af40-f16041f06157",
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "> hi\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Hello!\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "> u r name\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "None\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "> hello\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Hi there!\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "> what is your name\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "I am a chatbot created using NLP.\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "> hoe are you\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "None\n"
     ]
    }
   ],
   "source": [
    "import nltk\n",
    "from nltk.chat.util import Chat, reflections\n",
    "\n",
    "pairs = [\n",
    "    [r\"hi|hello\", [\"Hello!\", \"Hi there!\"]],\n",
    "    [r\"what is your name ?\", [\"I am a chatbot created using NLP.\"]],\n",
    "    [r\"how are you ?\", [\"I'm good. How can I help you?\"]],\n",
    "    [r\"quit\", [\"Goodbye!\"]]\n",
    "]\n",
    "\n",
    "chat = Chat(pairs, reflections)\n",
    "chat.converse()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "f1fc3f43-6080-4ff6-a3d0-13d4019c6528",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
