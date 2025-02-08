<p align="center">
  <img src="assets/diagram.png" 
</p>
  
## ☁️ 30 Days DevOps Challenge -   ☁️

This is part of the final project of the Multicloud, Devops and AI Challenge!

In this project I 


<h2>Environments and Technologies Used</h2>

  - Amazon Web Services (AWS)
  - RapidAPI



  
<h2>Key Features</h2>  

✅ 
✅ 
✅ 

<h2>Step by Step Instructions</h2>

***1. Repo and API configuration***

We will begin by setting up the environment and code that we will be utilizing. In this instance, we will use gitpod to create a new workspace and do the commands from there. We will be setting up an account with RapidAPI for our Premier League Standings data.

I created a .yml script for gitpod where it will automatically install AWS CLI and set the AWS credentials with the environment variables defined in Gitpod. This makes sure that our future projects are automated and we can start right away.

To achieve this, we will go to Gitpod's settings and set our credentials with the variables `AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY` and `AWS_DEFAULT_REGION` Respectively.

![image](/assets/image1.png)

Finally, we will make sure our dependencies are installed properly.

```
pip install boto3
pip install python-dotenv
pip install requests
```

***Option 2: Local AWS CLI Setup***

NOTE: Keep in mind this is for a Linux environment, check the AWS documentation to install it in your supported Os.

   ```
   curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
unzip awscliv2.zip
sudo ./aws/install
```
We then do `AWS configure` and enter our access and secret key along with the region. Output format set to JSON. With this command we will double check that our credentials are put in place for CLI:

```
aws sts get-caller-identity
```

And finally, we will also be installing `gettext` which is a command-line utility is used for environment variable substituition in shell scripts and text files.

```
sudo apt-get update 
sudo apt-get install gettext
```

***2.  Configuring and Creating .env file***

In this step we will be configurating and setting up the .env file that we will be using for this project. 


***3. Generate JSON files with Templates***



***4. Build and Push Docker Image***



***5. Create AWS Resources, Setting up EventBridge and Testing ECS Task - Final Result***


<h2>Conclusion</h2>

The successful completion of these integrations and deployments established CloudMart as a production-ready platform with robust analytics capabilities and scalable infrastructure.
