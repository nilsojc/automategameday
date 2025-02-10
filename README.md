<p align="center">
  <img src="assets/diagram.png" 
</p>
  
## ☁️ 30 Days DevOps Challenge -   ☁️

This is the 8th project for the 30 days DevOps All Star Challenge!

In this project I 


<h2>Environments and Technologies Used</h2>

  - Amazon Web Services (AWS)
  - RapidAPI
  - Terraform
  - Python
  - Gitpod
  



  
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

We will then install terraform CLI:

```
sudo wget -O - https://apt.releases.hashicorp.com/gpg | sudo gpg --dearmor -o /usr/share/keyrings/hashicorp-archive-keyring.gpg
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/hashicorp-archive-keyring.gpg] https://apt.releases.hashicorp.com $(lsb_release -cs) main" | sudo tee /etc/apt/sources.list.d/hashicorp.list
sudo apt update && sudo apt install terraform
```


Lastly, we will make sure we store our api key safely:

```
aws ssm put-parameter --name "nba-api-key" --value "<API_KEY>" --type "SecureString"
```

***2.  Run Terraform Commands ***

In this step we will be configurating and setting up the terraform commands to automate and create our resources! 


***3. Create SNS Topic and create a JSON policy***

Next, we will be creating the SNS topic along with creating the subscription for the topic and the JSON policy for publish!

```
aws sns create-topic --name gd_topic
```

It will display the ARN of the topic.

![image](/assets/image3.png)

Then, we will create a subscription with an Email and SMS protocol. Replace arn with user-generated topic arn as well as the email to be subscribed to and phone number.

```
aws sns subscribe \
    --topic-arn arn:aws:sns:us-east-1:123456789012:gd_topic \
    --protocol email \
    --notification-endpoint youremail.com
```

```
aws sns subscribe \
    --topic-arn arn:aws:sns:us-east-1:123456789012:gd_topic \
    --protocol sms \
    --notification-endpoint yourphonenumber
```
You can check the subscriptions on the CLI(Replace the topic ARN) or in the console.

```
aws sns list-subscriptions-by-topic \
    --topic-arn arn:aws:sns:us-east-1:123456789012:gd_topic

```

![image](/assets/image4.png)


This is how it will look like in the console.

![image](/assets/image5.png)

Next, we will create the sns publish policy.

```
aws iam create-policy \
    --policy-name gd_sns_policy \
    --policy-document '{
        "Version": "2012-10-17",
        "Statement": [
            {
                "Effect": "Allow",
                "Action": "sns:Publish",
                "Resource": "arn:aws:sns:us-east-1:123456789012:gd_topic"
            }
        ]
    }'
```

We can check if it was created successfully.

```
aws iam list-policies --query "Policies[?PolicyName=='gd_sns_policy']"
```

Finally, we will attach permissions to the SNS policy. "myrole" will be exchanged by the role created and we will set the policy arn of the previously created gd_sns_policy.

```
aws iam attach-role-policy \
    --role-name myrole \
    --policy-arn arn:aws:iam::123456789012:policy/gd_sns_policy
```


***4. Final Result - Test the Function**


We open the function and copy-paste the code from the repository (or you can fine-tune to your liking and modify)

![image](/assets/image7.png)

Before we deploy the function though, we set the environment variables.

![image](/assets/image7.png)

Finally, we test the result by creating a test event and testing it out.

![image](/assets/image9.png)
![image](/assets/image10.png)

And Voila! We now have the data with the names of the team, the score, and even the formations!

![image](/assets/image11.png)

NOTE: If there are no matches in a current date, for example, it can get no data therefore showing notifications like these:

![image](/assets/image12.png)

NOTE2: When there are a lot of dates involved, we might need to adjust the timeout so that the SNS i published with this command:

```
aws lambda update-function-



<h2>Conclusion</h2>


