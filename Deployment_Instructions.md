# AI Features and Deployment

Deployment of AI-powered features is optional. Students may instead deploy a version of their application without AI functionality.

# Hugging Face Inference API (Optional)

Students who wish to deploy AI-powered features will need to use a hosted embeddings service as the sentence-transformers approach used in the tutorials is generally too resource-intensive for a PythonAnywhere free account. 

[Hugging Face](https://huggingface.co/) Inference provides hosted access to AI models, allowing applications to generate embeddings and perform inference without needing to run models locally.

Any costs associated with third-party services are the responsibility of the student. In practice, costs are typically very low. The tutorial application was successfully deployed and tested within the free US$0.10 credit provided with a new Hugging Face account, with total usage costing approximately US$0.08. Most embeddings were generated locally, with the hosted API used only for testing queries and embedding a small number of additional destinations to demonstrate things working.

Students who intend to deploy and demonstrate AI-powered features are nevertheless encouraged to purchase a small amount of Hugging Face credit to avoid unexpected usage limits. Unfortunately, QUT-hosted embedding models cannot currently be used from PythonAnywhere because the university's custom API domain is not included on PythonAnywhere's allowlist.

# Important

There are no additional marks for deploying AI-powered features, and the use of paid services is entirely optional. Students will not be disadvantaged if their deployed application excludes AI functionality. An earlier version containing the core application features may be deployed, as the deployment assessment focuses on successfully configuring and deploying a dynamic web application.

# Other notes

Hugging Face is a widely adopted industry platform for AI development. It is often described as a "GitHub for machine learning models", providing a central repository where organisations and researchers can publish, share, discover, and use AI models. Many companies use Hugging Face to access pre-trained models and hosted inference services rather than building and hosting their own models from scratch.


