# AI-driven Influencer Marketing Platform

## About
AI-driven Influencer Marketing Platform is a platform that helps identify and manage influencer marketing campaigns.

## Getting Started
To get started, you need to have Python and pip installed on your system. Then, you can install the required packages by running the following command in your terminal:
bash
pip install -r requirements.txt

After that, you can run the application by using the following command:
bash
gunicorn --workers 3 app:app --bind 0.0.0.0:$PORT

Replace `$PORT` with your desired port number.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
This project is licensed under the MIT License.
