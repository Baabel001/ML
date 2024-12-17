import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import mean_absolute_error
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.pipeline import Pipeline
from typing import Dict, List, Any

class RegressionTester:
    """
    Classe pour tester des modèles de régression avec optimisation d'hyperparamètres via GridSearchCV.
    Inclut la normalisation/standardisation pour les modèles qui en ont besoin.
    """

    def __init__(self, X: pd.DataFrame, y: pd.Series, test_size: float = 0.2, random_state: int = 42):
        """
        Initialise les données d'entraînement et de test.
        """
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(
            X, y, test_size=test_size, random_state=random_state
        )
        self.models = {}
        self.best_models = {}
        self.results = {}
        

    def add_model(self, name: str, model, param_grid: Dict[str, List[Any]], preprocess: str = None):
        """
        Ajoute un modèle avec sa grille d'hyperparamètres et un éventuel prétraitement.
        :param name: Nom du modèle
        :param model: Instance du modèle
        :param param_grid: Grille d'hyperparamètres
        :param preprocess: 'standardize', 'normalize' ou None
        """
        if preprocess == "standardize":
            pipeline = Pipeline([
                ('scaler', StandardScaler()),
                ('model', model)
            ])
            # Adapter la grille d'hyperparamètres
            param_grid = {f"model__{k}": v for k, v in param_grid.items()}

        elif preprocess == "normalize":
            pipeline = Pipeline([
                ('scaler', MinMaxScaler()),
                ('model', model)
            ])
            param_grid = {f"model__{k}": v for k, v in param_grid.items()}

        else:
            pipeline = model

        self.models[name] = {"pipeline": pipeline, "param_grid": param_grid}

    def evaluate_models(self, cv: int = 5):
        """
        Entraîne et optimise chaque modèle avec GridSearchCV, puis calcule la MAE sur le test set.
        """
        for name, details in self.models.items():
            print(f"Optimisation et évaluation du modèle : {name}")

            # GridSearchCV pour optimiser les hyperparamètres
            grid_search = GridSearchCV(
                estimator=details["pipeline"],
                param_grid=details["param_grid"],
                scoring="neg_mean_absolute_error",
                cv=cv,
                verbose=1
            )
            grid_search.fit(self.X_train, self.y_train)

            # Meilleur modèle et prédictions
            best_model = grid_search.best_estimator_
            y_pred = best_model.predict(self.X_test)

            # Calcul de la Mean Absolute Error
            mae = mean_absolute_error(self.y_test, y_pred)

            # Stockage des résultats
            self.best_models[name] = best_model
            self.results[name] = {"MAE": mae, "Best Params": grid_search.best_params_}

    def compare_models(self):
        """
        Affiche les performances des modèles optimisés.
        """
        print("\n--- Comparaison des Modèles (MAE) ---")
        results_df = pd.DataFrame({
            name: {"MAE": details["MAE"], "Best Params": details["Best Params"]}
            for name, details in self.results.items()
        }).T
        print(results_df.sort_values(by="MAE", ascending=True))

    def get_results(self) -> Dict:
        """
        Retourne les résultats des évaluations.
        """
        return self.results