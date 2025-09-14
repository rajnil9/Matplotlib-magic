import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# -------------------------------
# 🎨 Styling (Light Theme)
# -------------------------------
plt.style.use("seaborn-v0_8-whitegrid")   # clean light theme

fig, ax = plt.subplots(figsize=(12, 6))
fig.patch.set_facecolor("#ffffff")        # figure background
ax.set_facecolor("#f9f9f9")               # axes background

# Line styles with markers
line1, = ax.plot([], [], label="Channel 1", color="#17bc4e", linewidth=2.5,marker="o", markersize=5)
line2, = ax.plot([], [], label="Channel 2", color="#ff320e", linewidth=2.5,marker="s", markersize=5)

# -------------------------------
# 🏷️ Labels & Title
# -------------------------------
ax.set_title("Live Data Stream", fontsize=20, fontweight="bold", color="#222222", pad=20)
ax.set_xlabel("Time", fontsize=14, color="#444444")
ax.set_ylabel("Values", fontsize=14, color="#444444")

# Grid & Legend
ax.grid(True, linestyle="--", alpha=0.6, color="#010A0E")
ax.legend(
    loc="upper left", fontsize=12, frameon=True, shadow=True, 
    facecolor="#ffffff", edgecolor="#0c0101"
)

# -------------------------------
# 🔄 Animation Function
# -------------------------------
def animate(i):
    try:
        data = pd.read_csv("data.csv")
    except Exception as e:
        print(f"Error reading CSV: {e}")
        return

    if data.empty:
        return

    # Only show last 50 points (sliding window)
    N = 50
    x = data["x_value"].tail(N)
    y1 = data["total_1"].tail(N)
    y2 = data["total_2"].tail(N)

    # Update the line objects
    line1.set_data(x, y1)
    line2.set_data(x, y2)

    # Adjust limits dynamically
    ax.relim()
    ax.autoscale_view()

# -------------------------------
# 🎥 Run Animation
# -------------------------------
ani = FuncAnimation(fig, animate, interval=1000, cache_frame_data=False)

plt.tight_layout()
plt.show()
