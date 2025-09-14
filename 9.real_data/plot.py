import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# =====================================================
# 🎨 PLOT STYLING (Light Theme)
# =====================================================
plt.style.use("seaborn-v0_8-whitegrid")     # use a clean light theme

# Create figure & axis
fig, ax = plt.subplots(figsize=(12, 6))

# Background colors
fig.patch.set_facecolor("#ffffff")          # overall figure background
ax.set_facecolor("#f9f9f9")                 # plotting area background

# Define two empty line objects (to be updated later)
line1, = ax.plot([], [], label="Channel 1", color="#17bc4e",
                 linewidth=2.5, marker="o", markersize=5)
line2, = ax.plot([], [], label="Channel 2", color="#ff320e",
                 linewidth=2.5, marker="s", markersize=5)

# =====================================================
# 🏷️ TITLES, LABELS & LEGEND
# =====================================================
ax.set_title("Live Data Stream", fontsize=20, fontweight="bold",
             color="#222222", pad=20)        # chart title
ax.set_xlabel("Time", fontsize=14, color="#444444")   # X-axis label
ax.set_ylabel("Values", fontsize=14, color="#444444") # Y-axis label

# Grid styling
ax.grid(True, linestyle="--", alpha=0.6, color="#010A0E")

# Legend styling
ax.legend(loc="upper left", fontsize=12, frameon=True, shadow=True,
          facecolor="#ffffff", edgecolor="#0c0101")

# =====================================================
# 🔄 ANIMATION FUNCTION
# =====================================================
def animate(i):
    """
    This function is called periodically by FuncAnimation.
    It:
      1. Reads the latest CSV data
      2. Selects the last N points (sliding window)
      3. Updates the line plots with new data
    """
    try:
        # Read the CSV file where data is being written
        data = pd.read_csv("data.csv")
    except Exception as e:
        print(f"Error reading CSV: {e}")
        return

    # Skip if CSV has no data yet
    if data.empty:
        return

    # Show only the last 50 rows for a smooth "live" effect
    N = 50
    x = data["x_value"].tail(N)
    y1 = data["total_1"].tail(N)
    y2 = data["total_2"].tail(N)

    # Update both line objects with new data
    line1.set_data(x, y1)
    line2.set_data(x, y2)

    # Dynamically adjust axes so data always fits
    ax.relim()
    ax.autoscale_view()

# =====================================================
# 🎥 RUN THE ANIMATION
# =====================================================
ani = FuncAnimation(fig, animate, interval=1000, cache_frame_data=False)

plt.tight_layout()
plt.show()
