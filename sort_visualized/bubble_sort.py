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
    iter_count = 0
    while sorted_index >= 0:
        iter_count += 1
        for i in range(sorted_index - 1):
            yield (data, iter_count, i, i + 1, sorted_index)
            if data[i] > data[i + 1]:
                data[i], data[i + 1] = data[i + 1], data[i]
                yield (data, iter_count, i + 1, i, sorted_index)
        sorted_index -= 1

    for i in range(10):  # Add frames of fully sorted to end
        yield (data, iter_count, 0, 0, 0)


def update(frame):
    """Frame is the (data, i, iter_count) tuple."""
    datums, iter_count, orange, red, sorted_index = frame
    ax.clear()
    bars = ax.bar(range(len(data)), datums)
    for k in range(len(data)):
        if k >= sorted_index:
            bars[k].set_color("green")
        elif k == orange or k == red:
            bars[k].set_color("orange")
        else:
            bars[k].set_color("blue")

    ax.set_title('Bubble Sort\nPass: {}'.format(iter_count))


animation = ani.FuncAnimation(
    fig,
    update,
    frames=bubble_sort_gen,
    interval=200,
    blit=False,
    repeat=False,
    save_count=10000,
)

animation.save(r"C:\Users\Patrick\Desktop\Demo.mp4")
# plt.show()
