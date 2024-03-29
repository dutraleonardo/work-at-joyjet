
# Joyjet Tech Interview

Thank you for coming to our tech-interview test page. Come and help us build game changing apps and platforms for international clients!
[Joyjet](http://joyjet.com) was created nearly 20 years ago in Paris and is now looking to grow it's team with highly skilled individuals! Today we are based in Paris (France) and Fortaleza (Brazil), and our teams speak five major languages.

## Guidelines

- [Duplicate](https://help.github.com/articles/duplicating-a-repository/) this repository (do **not** fork it);
- If you are responding to a backend position, please solve the levels inside backend in ascending order;
- Otherwise, you can use the appropriate folders for iOS, Android or front end;
- Feel free to complete tests for other platforms for extra brownie points;
- Commit at the very least at the end of each level.

## What we expect

- Clean code;
- Tests;
- Comments when you need to clarify a design decision or assumptions about the spec;
- A simple way to run the code and the tests.

## Acknowledgements

The Android, iOS, webdesign and frontend tests were completely designed by us, while the backend tests were shamesly ~~inspired~~ copied from the tests at one of our clients interview process, which our client had already found to be really great at another client. :)

## Project Documentation
### How to run
```
git clone https://github.com/dutraleonardo/work-at-joyjet
cd work-at-joyjet
pip install -r requirements.txt
python run.py
```

### MongoDB
* Make sure you have mongoDB installed and running
* Set enviroment variable: ``` export MONGO_URI=mongodb://yourmongodb:27017/dbname ```
* Create a collection named cart_checkout

### How to test?
* Send a POST request to API endpoint ``` /cart_checkout ```
* Put the json on body request
* Check response
* Check mongodb collection
* On app/ folder run: ```pytest``` to execute tests
