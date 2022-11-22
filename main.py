import filtering

################################################
#               Code skeleton
################################################

# current_position : [1 point (most probable), full map of probabilities (map_position_probabilities)]

# Get map from computer vision, starting position and goal position
world_map, current_pos, goal_pos = starting_map()

# Plan the optimal path based on current thymio position and goal position
optimal_path = global_planning(current_pos, goal_pos)

while goal is False:

    if obstacle: 
        local_avoidance()

    else:
        # Start following towards optimal path
        thymio_motion = move_thymio(current_pos, optimal_path)

    # Need to find back the position of the thymio to make sure Thymio is on track
    current_pos_motion = filtering.filtering_motion(map_position_probabilities, thymio_motion)
    # Get an estimation of Thymio position based on vision
    position_vision = get_thymio_pos()
    # Compare and adjust Thymio position with this new measurement
    current_pos = filtering.filtering_map(current_pos_motion, position_vision)

    optimal_path = after_motion(optimal_path, current_pos)