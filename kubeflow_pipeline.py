import kfp
from kfp import dsl

# Étape 1 : Définir les composants du pipeline
@dsl.component
def preprocess():
    return dsl.ContainerSpec(
        image="yassindoghri/mini-projet-model",
        command=["python", "preprocessing.py"]
    )

@dsl.component
def train():
    return dsl.ContainerSpec(
        image="yassindoghri/mini-projet-model",
        command=["python", "train.py"]
    )

@dsl.component
def evaluate():
    return dsl.ContainerSpec(
        image="yassindoghri/mini-projet-model",
        command=["python", "evaluate.py"]
    )

@dsl.component
def deploy():
    return dsl.ContainerSpec(
        image="yassindoghri/mini-projet-model",
        command=["python", "deploy.py"]
    )

# Définition du pipeline
@dsl.pipeline(
    name="House Price Prediction Pipeline",
    description="Un pipeline complet pour prédire les prix des maisons"
)
def house_price_pipeline():
    preprocess_task = preprocess()
    train_task = train().after(preprocess_task)
    evaluate_task = evaluate().after(train_task)
    deploy_task = deploy().after(evaluate_task)

# Compiler le pipeline en YAML
if __name__ == "__main__":
    kfp.compiler.Compiler().compile(house_price_pipeline, "house_price_pipeline.yaml")
