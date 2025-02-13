import kfp
from kfp import dsl

# Définir le pipeline
@dsl.pipeline(
    name="House Price Prediction Pipeline",
    description="Un pipeline complet pour prédire les prix des maisons"
)
def house_price_pipeline():
    # Étape 1 : Prétraitement des données
    preprocess = dsl.ContainerOp(
        name="preprocess",
        image="yassindoghri/preprocessing:v1",  # Remplacez par votre image Docker
        arguments=[],  # Ajoutez des arguments si nécessaire
    )

    # Étape 2 : Entraînement du modèle
    train = dsl.ContainerOp(
        name="train",
        image="yassindoghri/train:v1",  # Remplacez par votre image Docker
        arguments=[],  # Ajoutez des arguments si nécessaire
    ).after(preprocess)  # S'exécute après l'étape de prétraitement

    # Étape 3 : Évaluation du modèle
    evaluate = dsl.ContainerOp(
        name="evaluate",
        image="yassindoghri/evaluate:v1",  # Remplacez par votre image Docker
        arguments=[],  # Ajoutez des arguments si nécessaire
    ).after(train)  # S'exécute après l'étape d'entraînement

    # Étape 4 : Déploiement du modèle (API Flask)
    deploy = dsl.ContainerOp(
        name="deploy",
        image="yassindoghri/api-flask:v1",  # Remplacez par votre image Docker
        arguments=[],  # Ajoutez des arguments si nécessaire
    ).after(evaluate)  # S'exécute après l'étape d'évaluation

# Compiler le pipeline en YAML
if __name__ == "__main__":
    kfp.compiler.Compiler().compile(house_price_pipeline, 'house_price_pipeline.yaml')