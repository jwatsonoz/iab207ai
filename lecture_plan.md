
# Recordings

# Adding AI Features

Why AI in Web Applications?
  show examples
  AI is an enhancement layer - AI can enhance without replacing traditional functionality
  better user experience (slower, extra storage, increased complexity)

What are embeddings?
  Embeddings allow search based on meaning rather than exact words
  Limitations of keyword search e.g. "beach holiday" might miss "coastal getaway" due to words being different
  AI transforms text into vectors where similar meanings are close in the vector space
  Demonstrate *is there a visual way*?

How Might we add embeddings to a site?
  Architecture:
    Database Records
      e.g. title, description, category etc
    Generate Embeddings
    Store Vectors
    User QueryGenerate Query Embedding
    Compare Similarity
    Return Best Matches
    NB: generate embeddings for database records once during administration or data import (not every time!)
  Selecting a model (intro to Hugging Face)
    widely used AI model platform
    often described as GitHub for machine learning models
    same platform used for the Sentence Transformers library they have already used locally
    all-MiniLM-L6-v2
      small, fast, good quality, suitable for student projects

Demonstration of embeddings
  Installing sentence transformers
  Code walkthrough
  Testing data

Enhancing web application search with AI
  Code walkthrough

Deploy
Students may:

Deploy the application without AI features.
Demonstrate core functionality online.
Submit the fully functioning AI-enabled version separately for testing.

This aligns with industry practice where experimental or advanced features may not always be deployed in production environments.

Dynamic website deployment on PythonAnywhere (No AI - required as minimum)

Deployment with AI (entirely optional)






p2_How might we add embeddings to our site?
p3_Adding intelligent search to a website

# Deploying website
p4_Deploying a dynamic website to PythonAnywhere
p4_Deploying with AI Features (optional)

