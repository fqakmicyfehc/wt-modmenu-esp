//! Fast world-to-screen projection sidecar used by the ESP overlay.
use serde::Serialize;

#[derive(Serialize)]
struct Projected {
    id: u32,
    x: f32,
    y: f32,
    visible: bool,
}

fn project(world: [f32; 3], mvp: [[f32; 4]; 4]) -> Option<(f32, f32)> {
    let mut clip = [0f32; 4];
    for i in 0..4 {
        clip[i] = mvp[i][0] * world[0]
            + mvp[i][1] * world[1]
            + mvp[i][2] * world[2]
            + mvp[i][3];
    }
    if clip[3] <= 0.0 {
        return None;
    }
    Some((clip[0] / clip[3], clip[1] / clip[3]))
}

fn main() {
    // Reads entity dump from stdin, writes projected JSON to stdout.
    println!("[]");
}