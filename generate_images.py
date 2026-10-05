import matplotlib.pyplot as plt
import os
from PIL import Image

def save_plot_as_webp(fig, filename):
    filepath = f"images/blog/{filename}"
    fig.savefig(filepath, format='webp', bbox_inches='tight')
    print(f"Saved {filepath}")

def create_cpu_bottleneck_diagnosis():
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.bar(['CPU Core 1', 'CPU Core 2', 'GPU', 'RAM'], [100, 30, 40, 60], color=['#e74c3c', '#3498db', '#95a5a6', '#2ecc71'])
    ax.set_ylabel('Utilization (%)')
    ax.set_title('Classic CPU Bottleneck Profile')
    ax.set_ylim(0, 110)
    for i, v in enumerate([100, 30, 40, 60]):
        ax.text(i, v + 2, f"{v}%", ha='center', va='bottom')
    save_plot_as_webp(fig, "cpu-bottleneck-diagnosis.webp")
    plt.close(fig)

def create_cpu_vs_gpu_utilization():
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.plot([1, 2, 3, 4, 5], [95, 98, 100, 99, 100], label="CPU Usage", color='#e74c3c', marker='o')
    ax.plot([1, 2, 3, 4, 5], [45, 42, 40, 43, 38], label="GPU Usage", color='#3498db', marker='s')
    ax.set_xlabel('Time (Minutes)')
    ax.set_ylabel('Utilization (%)')
    ax.set_title('CPU Bottleneck Timeline')
    ax.legend()
    ax.set_ylim(0, 110)
    save_plot_as_webp(fig, "cpu-vs-gpu-utilization.webp")
    plt.close(fig)

def create_cpu_optimization_before_after():
    fig, ax = plt.subplots(figsize=(8, 5))
    width = 0.35
    labels = ['Before Optimize', 'After Optimize']
    fps = [45, 65]
    cpu = [100, 80]
    x = [0, 1]

    ax.bar([i - width/2 for i in x], fps, width, label='FPS', color='#2ecc71')
    ax.bar([i + width/2 for i in x], cpu, width, label='CPU Usage %', color='#e74c3c')

    ax.set_ylabel('Value')
    ax.set_title('Effect of CPU Optimization')
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.legend()
    save_plot_as_webp(fig, "cpu-optimization-before-after.webp")
    plt.close(fig)

def create_resolution_comparison():
    fig, ax = plt.subplots(figsize=(8, 5))
    resolutions = ['1080p', '1440p', '4K']
    cpu_usage = [85, 60, 40]
    gpu_usage = [65, 85, 99]

    ax.plot(resolutions, cpu_usage, marker='o', label='Typical CPU Demand', color='#e74c3c')
    ax.plot(resolutions, gpu_usage, marker='s', label='Typical GPU Demand', color='#3498db')

    ax.set_ylabel('Relative Demand (%)')
    ax.set_title('Hardware Demand Shifts with Resolution')
    ax.legend()
    save_plot_as_webp(fig, "1080p-vs-1440p-vs-4k-gaming-bottleneck.webp")
    plt.close(fig)

def create_cpu_gpu_workload_diagram():
    fig, ax = plt.subplots(figsize=(8, 5))

    # Simple conceptual stacked bar
    x = ['Engine/Logic (CPU)', 'Render/Pixels (GPU)']
    y1080 = [60, 40]
    y4k = [20, 80]

    ax.bar(x, y1080, label='1080p Profile', alpha=0.7)
    ax.bar(x, y4k, bottom=y1080, label='4K Profile', alpha=0.7)

    ax.set_ylabel('Frame Processing Time (%)')
    ax.set_title('Where Time is Spent Per Frame')
    ax.legend()
    save_plot_as_webp(fig, "cpu-gpu-workload-diagram.webp")
    plt.close(fig)

def create_resolution_infographic():
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.axis('off')
    ax.text(0.5, 0.8, "1080p = 2M Pixels (CPU works fast to feed GPU)", ha='center', fontsize=12, bbox=dict(facecolor='#eee', alpha=0.5))
    ax.text(0.5, 0.5, "1440p = 3.6M Pixels (Balanced Workload)", ha='center', fontsize=12, bbox=dict(facecolor='#ddd', alpha=0.5))
    ax.text(0.5, 0.2, "4K = 8.3M Pixels (GPU works hard on pixels)", ha='center', fontsize=12, bbox=dict(facecolor='#ccc', alpha=0.5))
    ax.set_title("Resolution Pixel Counts", pad=20)
    save_plot_as_webp(fig, "resolution-comparison-infographic.webp")
    plt.close(fig)

def create_ram_capacity_comparison():
    fig, ax = plt.subplots(figsize=(8, 5))
    categories = ['Windows + BG Apps', 'Modern Game', 'Total Usage', 'Capacity Left (16GB)', 'Capacity Left (32GB)']
    values = [4, 10, 14, 2, 18]
    colors = ['#95a5a6', '#e67e22', '#d35400', '#c0392b', '#27ae60']

    ax.barh(categories, values, color=colors)
    ax.set_xlabel('RAM (GB)')
    ax.set_title('Memory Usage Profile (Modern Gaming)')
    save_plot_as_webp(fig, "16gb-vs-32gb-vs-64gb-gaming-ram.webp")
    plt.close(fig)

def create_ram_usage_diagram():
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.pie([15, 60, 25], labels=['OS/System', 'Game Assets', 'Free/Cache'], autopct='%1.0f%%', colors=['#bdc3c7', '#3498db', '#2ecc71'])
    ax.set_title('Typical 32GB RAM Allocation During Gaming')
    save_plot_as_webp(fig, "ram-usage-diagram.webp")
    plt.close(fig)

def create_memory_pressure_visual():
    fig, ax = plt.subplots(figsize=(8, 5))
    x = [1, 2, 3, 4, 5]
    fps = [80, 78, 15, 75, 12] # Stuttering
    ax.plot(x, fps, color='#e74c3c', marker='x', linestyle='--', linewidth=2)
    ax.set_ylabel('FPS')
    ax.set_xlabel('Time')
    ax.set_title('Effect of Severe Memory Pressure (Paging/Stutter)')
    save_plot_as_webp(fig, "memory-pressure-visualization.webp")
    plt.close(fig)

def create_cpu_gpu_pairing():
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.scatter([1, 2, 3], [1, 2, 3], s=500, color='#2ecc71', label='Balanced')
    ax.scatter([1, 3], [3, 1], s=500, color='#e74c3c', marker='X', label='Mismatched')
    ax.set_xlabel('CPU Performance Tier')
    ax.set_ylabel('GPU Performance Tier')
    ax.set_title('CPU and GPU Pairing Matrix')
    ax.set_xticks([1,2,3])
    ax.set_yticks([1,2,3])
    ax.set_xticklabels(['Entry', 'Mid', 'High'])
    ax.set_yticklabels(['Entry', 'Mid', 'High'])
    ax.legend()
    save_plot_as_webp(fig, "cpu-gpu-pairing-diagram.webp")
    plt.close(fig)

def create_balanced_vs_mismatched():
    fig, ax = plt.subplots(figsize=(8, 5))
    x = ['Balanced System', 'CPU Bottleneck', 'GPU Bottleneck']
    cpu_util = [70, 100, 30]
    gpu_util = [95, 40, 99]
    width = 0.35

    ax.bar([i - width/2 for i in range(len(x))], cpu_util, width, label='CPU Usage %', color='#34495e')
    ax.bar([i + width/2 for i in range(len(x))], gpu_util, width, label='GPU Usage %', color='#f1c40f')

    ax.set_ylabel('Utilization')
    ax.set_title('System Balance Profiles')
    ax.set_xticks(range(len(x)))
    ax.set_xticklabels(x)
    ax.legend()
    save_plot_as_webp(fig, "balanced-vs-mismatched-pc.webp")
    plt.close(fig)

def create_compatibility_tree():
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.axis('off')
    ax.text(0.5, 0.9, "Target Resolution?", ha='center', fontsize=14, fontweight='bold')
    ax.text(0.2, 0.6, "1080p\n(Needs strong CPU)", ha='center', fontsize=12, bbox=dict(facecolor='#add8e6', edgecolor='blue', boxstyle='round,pad=1'))
    ax.text(0.8, 0.6, "4K\n(Needs strong GPU)", ha='center', fontsize=12, bbox=dict(facecolor='#ffcccb', edgecolor='red', boxstyle='round,pad=1'))

    ax.annotate('', xy=(0.3, 0.7), xytext=(0.5, 0.85), arrowprops=dict(arrowstyle="->", color="black"))
    ax.annotate('', xy=(0.7, 0.7), xytext=(0.5, 0.85), arrowprops=dict(arrowstyle="->", color="black"))

    ax.set_title("Basic Pairing Decision Tree")
    save_plot_as_webp(fig, "compatibility-decision-tree.webp")
    plt.close(fig)

def create_low_gpu_utilization_troubleshooting():
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.axis('off')
    ax.text(0.5, 0.9, "GPU Usage < 80%", ha='center', fontsize=14, fontweight='bold', bbox=dict(facecolor='yellow'))

    ax.text(0.2, 0.5, "Check CPU Usage\n(Is it 100% on a core?)", ha='center', bbox=dict(facecolor='#eee', boxstyle='round'))
    ax.text(0.8, 0.5, "Check FPS Caps\n(V-Sync on?)", ha='center', bbox=dict(facecolor='#eee', boxstyle='round'))
    ax.text(0.5, 0.2, "Check Temps\n(Is GPU throttling?)", ha='center', bbox=dict(facecolor='#eee', boxstyle='round'))

    ax.annotate('', xy=(0.3, 0.6), xytext=(0.45, 0.85), arrowprops=dict(arrowstyle="->"))
    ax.annotate('', xy=(0.7, 0.6), xytext=(0.55, 0.85), arrowprops=dict(arrowstyle="->"))
    ax.annotate('', xy=(0.5, 0.3), xytext=(0.5, 0.8), arrowprops=dict(arrowstyle="->"))

    ax.set_title("Low GPU Usage Checklist")
    save_plot_as_webp(fig, "low-gpu-utilization-troubleshooting.webp")
    plt.close(fig)

def create_cpu_limited_vs_gpu_limited():
    fig, ax = plt.subplots(1, 2, figsize=(10, 5))

    # CPU limited
    ax[0].bar(['CPU', 'GPU'], [100, 45], color=['#e74c3c', '#95a5a6'])
    ax[0].set_title('CPU Limited')
    ax[0].set_ylim(0, 110)

    # GPU limited
    ax[1].bar(['CPU', 'GPU'], [60, 99], color=['#95a5a6', '#2ecc71'])
    ax[1].set_title('GPU Limited')
    ax[1].set_ylim(0, 110)

    fig.suptitle('Hardware Limitation Types')
    save_plot_as_webp(fig, "cpu-limited-vs-gpu-limited-visual.webp")
    plt.close(fig)

def create_gpu_monitoring_example():
    fig, ax = plt.subplots(figsize=(8, 5))
    times = [0, 10, 20, 30, 40]
    gpu_usage = [99, 98, 45, 42, 99]

    ax.plot(times, gpu_usage, color='#9b59b6', linewidth=2, marker='o')
    ax.axvspan(20, 30, color='red', alpha=0.2, label='Low GPU Usage Spike')

    ax.set_xlabel('Time (s)')
    ax.set_ylabel('GPU Usage %')
    ax.set_title('Monitoring GPU Usage Drops')
    ax.legend()
    ax.set_ylim(0, 110)
    save_plot_as_webp(fig, "gpu-monitoring-example.webp")
    plt.close(fig)

def create_cpu_vs_gpu_bottleneck_comparison():
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.axis('tight')
    ax.axis('off')

    table_data = [
        ["Symptom", "CPU Bottleneck", "GPU Bottleneck"],
        ["GPU Usage", "Low (<90%)", "High (95-100%)"],
        ["CPU Usage", "High (Overall or per-core)", "Low to Moderate"],
        ["Resolution Effect", "Lowering Res = No FPS gain", "Lowering Res = Huge FPS gain"],
        ["Stuttering", "Common (1% lows drop)", "Less common (smooth but low FPS)"]
    ]

    table = ax.table(cellText=table_data, loc='center', cellLoc='center')
    table.auto_set_font_size(False)
    table.set_fontsize(11)
    table.scale(1, 2)

    save_plot_as_webp(fig, "cpu-vs-gpu-bottleneck-symptoms-comparison.webp")
    plt.close(fig)

def create_diagnostic_flowchart():
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.axis('off')

    ax.text(0.5, 0.9, "Are you hitting Target FPS?", ha='center', bbox=dict(boxstyle='round,pad=1', facecolor='lightblue'))
    ax.text(0.2, 0.6, "YES\nEnjoy Game!", ha='center', bbox=dict(boxstyle='round,pad=1', facecolor='lightgreen'))
    ax.text(0.8, 0.6, "NO\nCheck GPU Usage", ha='center', bbox=dict(boxstyle='round,pad=1', facecolor='lightpink'))

    ax.text(0.6, 0.3, "GPU > 95%\nGPU Bottleneck", ha='center', bbox=dict(boxstyle='round,pad=1', facecolor='orange'))
    ax.text(1.0, 0.3, "GPU < 90%\nLikely CPU Limit", ha='center', bbox=dict(boxstyle='round,pad=1', facecolor='orange'))

    ax.annotate('', xy=(0.3, 0.7), xytext=(0.45, 0.85), arrowprops=dict(arrowstyle="->"))
    ax.annotate('', xy=(0.7, 0.7), xytext=(0.55, 0.85), arrowprops=dict(arrowstyle="->"))

    ax.annotate('', xy=(0.6, 0.45), xytext=(0.75, 0.55), arrowprops=dict(arrowstyle="->"))
    ax.annotate('', xy=(0.95, 0.45), xytext=(0.85, 0.55), arrowprops=dict(arrowstyle="->"))

    ax.set_title("Basic Bottleneck Flowchart")
    save_plot_as_webp(fig, "bottleneck-diagnostic-flowchart.webp")
    plt.close(fig)

def create_utilization_frametime_visual():
    fig, ax1 = plt.subplots(figsize=(8, 5))

    time = [1, 2, 3, 4, 5, 6, 7]
    gpu_util = [99, 98, 40, 42, 99, 98, 99]
    frametime = [16, 16, 45, 42, 16, 16, 16]

    ax1.plot(time, gpu_util, 'b-', label='GPU Usage %')
    ax1.set_xlabel('Time')
    ax1.set_ylabel('Usage %', color='b')
    ax1.tick_params('y', colors='b')
    ax1.set_ylim(0, 110)

    ax2 = ax1.twinx()
    ax2.plot(time, frametime, 'r--', label='Frame Time (ms)')
    ax2.set_ylabel('Frame Time (ms)', color='r')
    ax2.tick_params('y', colors='r')

    fig.suptitle('How GPU Usage Drops Cause Frame Time Spikes')

    # Combined legend
    lines, labels = ax1.get_legend_handles_labels()
    lines2, labels2 = ax2.get_legend_handles_labels()
    ax2.legend(lines + lines2, labels + labels2, loc='upper right')

    save_plot_as_webp(fig, "utilization-frame-time-visual.webp")
    plt.close(fig)

if __name__ == "__main__":
    os.makedirs("images/blog", exist_ok=True)

    # Art 1: CPU Bottleneck
    create_cpu_bottleneck_diagnosis()
    create_cpu_vs_gpu_utilization()
    create_cpu_optimization_before_after()

    # Art 2: Resolution
    create_resolution_comparison()
    create_cpu_gpu_workload_diagram()
    create_resolution_infographic()

    # Art 3: RAM
    create_ram_capacity_comparison()
    create_ram_usage_diagram()
    create_memory_pressure_visual()

    # Art 4: Compatibility
    create_cpu_gpu_pairing()
    create_balanced_vs_mismatched()
    create_compatibility_tree()

    # Art 5: Low GPU Usage
    create_low_gpu_utilization_troubleshooting()
    create_cpu_limited_vs_gpu_limited()
    create_gpu_monitoring_example()

    # Art 6: CPU vs GPU Symptoms
    create_cpu_vs_gpu_bottleneck_comparison()
    create_diagnostic_flowchart()
    create_utilization_frametime_visual()

    print("All images generated.")
