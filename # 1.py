# 1. Data
data = [
    [1, 2], [2, 3], [2, 1],
    [8, 8], [9, 10], [10, 8]
]

# 2. Initial centroids
centroids = [[1, 2], [8, 8]]

# 3. Repeat the algorithm
for _ in range(100):

    labels = []

    # Assign each point to the nearest centroid
    for point in data:

        distances = []

        for center in centroids:
            d = ((point[0] - center[0]) ** 2 +
                 (point[1] - center[1]) ** 2)

            distances.append(d)

        labels.append(distances.index(min(distances)))

    # Calculate new centroids
    new_centroids = []

    for i in range(2):

        points = [data[j] for j in range(len(data)) if labels[j] == i]

        if len(points) > 0:
            x = sum(p[0] for p in points) / len(points)
            y = sum(p[1] for p in points) / len(points)

            new_centroids.append([x, y])
        else:
            new_centroids.append(centroids[i])

    # Check if centroids changed
    if new_centroids == centroids:
        break

    centroids = new_centroids

# 4. Print results
for i in range(2):
    cluster = [data[j] for j in range(len(data)) if labels[j] == i]

    print("Cluster", i + 1, ":", cluster)
    print("Centroid:", centroids[i])