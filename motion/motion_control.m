function [] = motion_control(start, goal, params)

% Parameters:
%   o start = [start_x; start_y; start_theta]
%   o goal = [goal_x; goal_y; goal_theta]
%   o params : struct with all constants

pos_ref = goal;
pos_current = start;

while pos_ref ~= pos_current
    pos_error = pos_ref - pos_current;
    % q = [v; omega]
    q = [ v_ref*cos(theta_error) + Kx*x_error;
          omega_ref + v_ref*(Ky*y_error + Ktheta*sin(theta_error)];
          
end