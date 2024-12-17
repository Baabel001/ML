from sklearn.neighbors import KNeighborsRegressor
from sklearn.svm import SVR
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import Ridge, Lasso, LinearRegression, ElasticNet, ElasticNetCV
from sklearn.tree import DecisionTreeRegressor
from xgboost import XGBRegressor
import pandas as pd
from sklearn.model_selection import StratifiedKFold

from models import RegressionTester
from preprocessing import final_data

def main():
    # Exemple d'utilisation avec un jeu de données fictif
    from sklearn.datasets import load_diabetes

    # Charger un jeu de données
    data = final_data
    # X = pd.DataFrame(data.data, columns = data.feature_names)
    # y = pd.Series(data.target)
    y = final_data["Y"].copy()
    X = final_data.drop(["Y", 'X4', 'X38'], axis = 1).copy()

    # kf = StratifiedKFold(n_splits = 10, shuffle = True, random_state = 42)
    
    # Initialiser l'instance de RegressionTester
    tester = RegressionTester(X, y)

    # Ajouter des modèles avec leurs grilles d'hyperparamètres et prétraitements
    
    tester.add_model("KNN", KNeighborsRegressor(), param_grid={
        "n_neighbors": [3, 5, 7],
        "weights": ["uniform", "distance"]
    }, preprocess="standardize")
    """
    tester.add_model("SVR", SVR(), param_grid={
        "C": [1, 10, 100],
        "epsilon": [0.1, 0.2, 0.5]
    }, preprocess="standardize")

    tester.add_model("Random Forest", RandomForestRegressor(), param_grid={
        "n_estimators": [50, 100],
        "max_depth": [None, 10],
    })
    """
    tester.add_model("Linear Regression", LinearRegression(), param_grid={})
    """
    tester.add_model("Decision Tree", DecisionTreeRegressor(), param_grid={
        "max_depth": [None, 5, 10],
        "min_samples_split": [2, 5]
    })
    
    tester.add_model("XGBoost", XGBRegressor(), param_grid={
        "n_estimators": [50, 100],
        "learning_rate": [0.01, 0.1],
        "max_depth": [3, 5]
    })
    """
    tester.add_model("Ridge", Ridge(), param_grid={
        "alpha": [.001,.01,.1,.2, .5, 1, 2, 5, 10, 20 , 50,100, 200, 500]
    }, preprocess="standardize")

    tester.add_model("Lasso", Lasso(), param_grid={
        "alpha": [.001,.01,.1,.2, .5, 1, 2, 5, 10, 20 , 50,100, 200, 500]
    }, preprocess="standardize")
    """
    tester.add_model("ElasticNet", ElasticNetCV(), param_grid={
        "alpha": [.001,.01,.1,.2, .5, 1, 2, 5, 10, 20 , 50,100, 200, 500]
    }, preprocess="standardize")
    """
    # Optimiser et évaluer les modèles
    tester.evaluate_models()

    # Comparer les modèles
    tester.compare_models()
    
    return tester.results

if __name__ == "__main__":
    main()