import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Create a new figure
fig, ax = plt.subplots()

# Set limits and remove axes
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.axis('off')

# Draw the robot head
robot_head = patches.Rectangle((4.5, 8), 1, 1, fill=True, color='gray', edgecolor='black')
ax.add_patch(robot_head)

# Draw the eyes
left_eye = patches.Circle((4.75, 8.75), 0.1, fill=True, color='white', edgecolor='black')
right_eye = patches.Circle((5.25, 8.75), 0.1, fill=True, color='white', edgecolor='black')
ax.add_patch(left_eye)
ax.add_patch(right_eye)

# Draw the mouth
mouth = patches.Rectangle((4.75, 8.25), 0.5, 0.1, fill=True, color='black')
ax.add_patch(mouth)

# Draw the robot body
robot_body = patches.Rectangle((4.25, 6), 1.5, 2, fill=True, color='gray', edgecolor='black')
ax.add_patch(robot_body)

# Draw the robot arms
left_arm = patches.Rectangle((3.75, 6.5), 0.5, 0.25, fill=True, color='gray', edgecolor='black')
right_arm = patches.Rectangle((5.75, 6.5), 0.5, 0.25, fill=True, color='gray', edgecolor='black')
ax.add_patch(left_arm)
ax.add_patch(right_arm)

# Draw the typewriter
typewriter = patches.Rectangle((3.5, 5), 3, 1, fill=True, color='black', edgecolor='black')
ax.add_patch(typewriter)
keys = patches.Rectangle((4, 5), 2, 0.5, fill=True, color='gray', edgecolor='black')
ax.add_patch(keys)

# Draw the paper
paper = patches.Rectangle((4.25, 6.5), 1.5, 0.75, fill=True, color='white', edgecolor='black')
ax.add_patch(paper)

# Add text to the paper to simulate typing
ax.text(4.5, 7, "Dear Diary,", fontsize=10, color='black')
ax.text(4.5, 6.75, "Today I learned", fontsize=10, color='black')
ax.text(4.5, 6.5, "Python!", fontsize=10, color='black')

# Show the plot
plt.gca().set_aspect('equal', adjustable='box')
plt.show()
