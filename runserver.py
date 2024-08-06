from API import create_app

from API.config.config import config_dict


app = create_app(config=config_dict["dev"])

if __name__=="__main__":
    app.run(app,debug=True)
