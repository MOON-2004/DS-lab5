import numpy as np
import matplotlib.pyplot as plt

# Generate 1000 dice rolls
rolls = np.random.randint(1, 7, size=1000)

# Print first 10 rolls
print("First 10 rolls:", rolls[:10])

# Find unique faces and their counts
faces, counts = np.unique(rolls, return_counts=True)

# Theoretical probability of each face
theoretical_probability = 1 / 6

print("\nFace Count Empirical P Theoretical P")

# Print probability information
for face, count in zip(faces, counts):
    empirical_probability = count / 1000

    print(
        face,
        count,
        round(empirical_probability, 4),
        round(theoretical_probability, 4)
    )

# Plot histogram
plt.hist(
    rolls,
    bins=np.arange(0.5, 7.5, 1),
    edgecolor="black"
)

plt.xlabel("Die Face")
plt.ylabel("Frequency")
plt.title("Dice Rolls Distribution")

# Save the graph
plt.savefig("die_rolls.png")

print("\nSaved die_rolls.png")

# Display the graph
plt.show()