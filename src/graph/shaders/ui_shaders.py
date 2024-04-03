# Default UI shaders
# Passing vertex, color seperately
VERTEX_SHADER = """
#version 330 core

layout(location = 0) in vec3 vertex;
layout(location = 1) in vec4 color;

out vec4 out_color;

void main() {
    gl_Position = vec4(vertex, 1.0);
    out_color = color; 
}

"""

FRAGMENT_SHADER = """
#version 330 core

out vec4 fragColor;
in vec4 out_color;

void main() {
    fragColor = out_color;
}

"""
