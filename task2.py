import matplotlib.pyplot as plt
import numpy as np

def koch_snowflake(order, size=300):
    """Generate points for Koch Snowflake."""
    def rotate(p, degrees):
        theta = np.radians(degrees)
        c, s = np.cos(theta), np.sin(theta)
        R = np.array([[c, -s], [s, c]])
        return np.dot(p, R)

    # Start with an equilateral triangle
    one_third = size / 3
    root_three = np.sqrt(3)

    # Initial triangle vertices
    points = np.array([
        [0, -size / (2 * root_three)],
        [size / 2, size / (2 * root_three)],
        [-size / 2, size / (2 * root_three)],
        [0, -size / (2 * root_three)]  # close the triangle
    ])

    def koch_curve(p1, p2, depth):
        if depth == 0:
            return [p1, p2]
        else:
            # Divide the line into three segments
            d = (p2 - p1) / 3
            pA = p1 + d
            pB = p1 + 2 * d

            # Calculate the peak of the 'triangle'
            peak = pA + rotate(d, 60)

            # Recursive calls for each segment
            result = []
            result.extend(koch_curve(p1, pA, depth - 1))
            result.extend(koch_curve(pA, peak, depth - 1))
            result.extend(koch_curve(peak, pB, depth - 1))
            result.extend(koch_curve(pB, p2, depth - 1))
            return result

    # Generate the snowflake
    snowflake_points = []
    for i in range(3):
        p1 = points[i]
        p2 = points[i + 1]
        if i < 2:  # Exclude the last point for the first two sides
            snowflake_points.extend(koch_curve(p1, p2, order)[:-1])
        else:  # Include the last point for the last side
            snowflake_points.extend(koch_curve(p1, p2, order))

    return snowflake_points

def plot_koch_snowflake(order):
    """Plot the Koch snowflake with a given recursion depth."""
    points = koch_snowflake(order)
    points = np.array(points)
    plt.figure(figsize=(8, 8))
    plt.plot(points[:, 0], points[:, 1], color='blue')
    plt.title(f'Koch Snowflake of Order {order}')
    plt.axis('equal')
    plt.axis('off')
    plt.show()

# Prompt user for the recursion depth
order = int(input("Please enter the recursion depth for the Koch Snowflake: "))
plot_koch_snowflake(order)
