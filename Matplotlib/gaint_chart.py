import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.patches import Patch
import numpy as np
from io import StringIO

# Read the data
data = """Task,Assignee,Start,Duration (weeks)
Literature Review,All,Week 1,2
System Architecture Design,Deepesh/Harsh,Week 2,2
EMG Signal Acquisition Setup,Deepesh,Week 3,2
Signal Processing Algorithm Development,Deepesh,Week 4,3
Machine Learning Model Development,Harsh,Week 5,4
Mechanical System Design,Yogendra,Week 3,4
Control System Integration,Harsh,Week 7,3
Prototype Assembly,Yogendra,Week 8,3
Initial Testing and Calibration,All,Week 11,2
Performance Optimization,Deepesh/Harsh,Week 13,3
User Interface Development,Harsh,Week 15,2
Documentation and Reporting,Ritesh,Week 1,24
Project Management,Ritesh,Week 1,24
Final Testing and Validation,All,Week 22,3
Preparation for Presentation/Demo,All,Week 25,2"""

# Convert the string data to a DataFrame
df = pd.read_csv(StringIO(data))

# Convert 'Start' to numeric weeks
df['Start'] = df['Start'].str.extract(r'(\d+)').astype(int)

# Calculate end week for each task
df['End'] = df['Start'] + df['Duration (weeks)'] - 1

# Set up color mapping for assignees
colors = plt.cm.get_cmap('Set3')(np.linspace(0, 1, len(df['Assignee'].unique())))
color_map = dict(zip(df['Assignee'].unique(), colors))

# Create the plot
fig, ax = plt.subplots(figsize=(15, 10))

# Plot the tasks
for idx, task in df.iterrows():
    ax.barh(task['Task'], task['Duration (weeks)'], left=task['Start']-1, color=color_map[task['Assignee']], alpha=0.8)
    ax.text(task['Start']-1, idx, f"{task['Start']}", va='center', ha='right', fontweight='bold')
    ax.text(task['End'], idx, f"{task['End']}", va='center', ha='left', fontweight='bold')

# Customize the plot
ax.set_yticks(range(len(df)))
ax.set_yticklabels(df['Task'])
ax.set_xlabel('Weeks')
ax.set_title('Project Gantt Chart')
ax.grid(True, axis='x', alpha=0.5)

# Add a legend
legend_elements = [Patch(facecolor=color_map[name], label=name) for name in color_map]
ax.legend(handles=legend_elements, title='Assignee', loc='center left', bbox_to_anchor=(1, 0.5))

# Adjust layout and display the plot
plt.tight_layout()
plt.show()