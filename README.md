# Treebank
This prototype builds a grammar tree and calculates a probability context free grammar from an audio file.

# Components
- Stanford Parser Server
- Main System with API
- Web App Server

# Processes
1. Input audio
1. Convert speech to text using Sphinx or Houndify
1. Preprocess sentences
1. Tokenize sentences
1. Tokenize words in each sentence
1. Tag part-of-speech on each word
1. Tag named entities
1. Tag “Mapua” named entities
1. Build grammar tree for each parsed sentence
1. Induce PCFG from a list of productions
1. Save trees as images

# Database
- audio_bin  
- speech_text  
- pos_tagged  
- named_entities  
- productions  
- pcfg  
- tree_bin  
- created  