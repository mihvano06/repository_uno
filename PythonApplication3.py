#####1 var.1
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn import datasets
import pandas as pd
iris = datasets.load_iris()
iris_data = pd.DataFrame(data=iris.data, columns=iris.feature_names)
iris_data['species'] = iris.target
iris_data['species'] = iris_data['species'].map({0: 'setosa', 1: 'versicolor', 2: 'virginica'})
plt.figure(figsize=(10, 6))
sns.scatterplot(data=iris_data,
                 x='sepal length (cm)',
                 y='sepal width (cm)',
                 hue='species',
                 style='species',
                 palette='deep')
plt.title("Iris Sepal Size")
plt.xlabel("Sepal length (cm)")
plt.ylabel("Sepal width (cm)")
plt.legend(title='Species')
plt.show()

#####2
import matplotlib.pyplot as plt
from statsmodels.datasets import nile
data = nile.load_pandas().data
data.set_index('year', inplace=True)
plt.figure(figsize=(10, 6))
plt.plot(data['volume'], label='Годовой расход воды в реке Нил')
plt.title('Годовой расход воды в реке Нил (1871-1970)')
plt.xlabel('Год')
plt.ylabel('Годовой расход воды (кубические гектометры)')
plt.legend()
plt.grid(True)
plt.show()



