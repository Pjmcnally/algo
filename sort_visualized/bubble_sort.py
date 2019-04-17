"""Visualization of the bubble sort algorithm.

For reference:
https://matplotlib.org/2.1.2/gallery/animation/basic_example_writer_sgskip.html
https://github.com/snorthway/algo-viz/blob/master/bubble_sort.py
"""

from random import shuffle
import matplotlib.pyplot as plt
import matplotlib.animation as ani

# Create a list of random integers between 0 and 100
sorted_data = list(range(1, 16))
data = sorted_data.copy()
shuffle(data)

# Create the figure
fig, ax = plt.subplots()
ax.axes.get_xaxis().set_visible(False)
ax.axes.get_yaxis().set_visible(False)


def bubble_sort_gen():
    """Yield current state of bubble sort."""
    sorted_index = len(data)
    swapped = True
    while swapped:
        swapped = False
        for i in range(sorted_index - 1):
            yield (data, i, i + 1, sorted_index)
            if data[i] > data[i + 1]:
                swapped = True
                data[i], data[i + 1] = data[i + 1], data[i]
                yield (data, i + 1, i, sorted_index)
        sorted_index -= 1

    for i in range(10):  # Add frames of fully sorted to end
        yield (data, 0, 0, 0)


def cocktail_shaker_gen():
    """Yield current state of bubble sort."""
    sorted_index_high = len(data)
    sorted_index_low = -1
    swapped = True
    while swapped:
        swapped = False
        for i in range(sorted_index_low + 1, sorted_index_high - 1):
            yield (data, i, i + 1, sorted_index_low, sorted_index_high)
            if data[i] > data[i + 1]:
                swapped = True
                data[i], data[i + 1] = data[i + 1], data[i]
                yield (data, i + 1, i, sorted_index_low, sorted_index_high)
        sorted_index_high -= 1
        if not swapped:
            break

        swapped = False
        for i in range(sorted_index_high - 1, sorted_index_low + 1, -1):
            yield (data, i, i - 1, sorted_index_low, sorted_index_high)
            if data[i] < data[i - 1]:
                swapped = True
                data[i], data[i - 1] = data[i - 1], data[i]
                yield (data, i - 1, i, sorted_index_low, sorted_index_high)
        sorted_index_low += 1

    for i in range(10):  # Add frames of fully sorted to end
        yield (data, 0, 0, 0, 0)


def update(frame):
    """Frame is the (data, i, iter_count) tuple."""
    datums, orange, red, sorted_index_low, sorted_index_high = frame
    ax.clear()
    bars = ax.bar(range(len(data)), datums)
    for k in range(len(data)):
        if k <= sorted_index_low or k >= sorted_index_high:
            bars[k].set_color("green")
        elif k == orange or k == red:
            bars[k].set_color("orange")
        else:
            bars[k].set_color("blue")

    ax.set_title('Bubble Sort')


animation = ani.FuncAnimation(
    fig,
    update,
    frames=cocktail_shaker_gen,
    interval=200,
    blit=False,
    repeat=False,
    save_count=10000,
)

# animation.save(r"C:\Users\Patrick\Desktop\Demo.mp4")
plt.show()
