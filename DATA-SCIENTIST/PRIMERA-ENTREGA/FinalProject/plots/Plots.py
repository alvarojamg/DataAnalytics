





# Crear una figura con subplots
# fig, axes = plt.subplots(2, 1, figsize=(10, 8))  # 2 filas, 1 columna
#
# # Gráfico 1: Estudiantes por rango de horas estudiadas
# count_range.plot(kind='bar', color='skyblue', ax=axes[0], legend=False)
# axes[0].set_title('Estudiantes por Rango de Horas Estudiadas')
# axes[0].set_xlabel('Rangos de Horas')
# axes[0].set_ylabel('Número de Estudiantes')
# axes[0].set_xticks(range(len(count_range)))
# axes[0].set_xticklabels(count_range.index, rotation=0)
#
# # Gráfico 2: Estudiantes por rango de scores
# count_scores.plot(kind='bar', color='orange', ax=axes[1], legend=False)
# axes[1].set_title('Estudiantes por Rango de Scores')
# axes[1].set_xlabel('Rangos de Scores')
# axes[1].set_ylabel('Número de Estudiantes')
# axes[1].set_xticks(range(len(count_scores)))
# axes[1].set_xticklabels(count_scores.index, rotation=0)
#
# # Ajustar el diseño
# plt.tight_layout()
# plt.show()