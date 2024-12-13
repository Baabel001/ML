from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error


def ajust_model(model:str, x_train, y_train, x_test):
    
    model_fit = model().fit(x_train, y_train)
    return model_fit.predict(x_test)

def score_model(predictions, y_test):
    return mean_absolute_error(y_test, predictions)