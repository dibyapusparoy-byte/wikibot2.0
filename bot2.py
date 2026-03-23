# filename: class11_12_bot_dict_only.py
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

# ====== CONFIG ======
TOKEN = "8784516259:AAE2030kvj3TUI24myprFXSbJG8lDzDZYqs"  # Telegram bot token

# ====== Predefined Class 11-12 Topics with 4-5 line definitions + examples ======
topics_dict = {
    # ======== CLASS 11 PHYSICS ========
    "measurement": """Fundamental and derived units used to quantify physical phenomena.
Points:
- Accuracy vs Precision: Accuracy is how close a measurement is to the true value.
- Dimensional Analysis: Using dimensions (M, L, T) to check equation correctness.
- Significant Figures: Digits that carry meaningful contributions to resolution.

Examples:
- Using a Vernier Caliper for diameter measurements.
- Converting units using dimensional consistency.""",

    "kinematics": """The study of motion without considering its causes (forces).
Points:
- Frame of Reference: The coordinate system from which motion is observed.
- Projectile Motion: Objects moving in a parabolic path under gravity.
- Relative Velocity: Velocity of an object as observed from a moving frame.

Examples:
- A ball thrown at an angle for maximum range.
- A swimmer crossing a flowing river.""",

    "motion laws": """Principles governing the relationship between a body and the forces acting on it.
Points:
- Inertia: The property of an object to resist changes in its state of motion.
- Impulse: The product of a large force and the short time it acts.
- Friction: Force opposing relative motion (static, kinetic, or rolling).

Examples:
- Recoil of a gun (Conservation of Momentum).
- Banking of roads for safe vehicle turning.""",

    "work energy": """Scalar quantities associated with the motion and configuration of objects.
Points:
- Work-Energy Theorem: Work done by net force equals change in kinetic energy.
- Conservative Forces: Forces where work depends only on start and end points.
- Energy Conservation: Energy is only transformed, never created or destroyed.

Examples:
- A compressed spring storing potential energy.
- A motor lifting a heavy load.""",

    "rotation": """Dynamics of systems rotating about a fixed axis.
Points:
- Center of Mass: Point where the entire mass of a system is concentrated.
- Torque: The rotational analogue of force causing angular acceleration.
- Moment of Inertia: Resistance of a body to rotational motion changes.

Examples:
- A figure skater spinning with pulled-in arms.
- Using a wrench to loosen a tight bolt.""",

    "gravitation": """The universal force of attraction between all matter.
Points:
- Kepler’s Laws: Three laws describing planetary orbital motion.
- Gravity (g): Acceleration due to Earth's pull, varying with height/depth.
- Escape Velocity: Minimum speed needed to break free from gravity.

Examples:
- Satellites in geostationary orbit.
- Tides caused by the Moon's pull.""",

    "bulk matter": """Mechanical and thermal behavior of solids, liquids, and gases.
Points:
- Hooke’s Law: Stress is proportional to strain within elastic limits.
- Bernoulli’s Principle: High fluid speed results in low pressure.
- Surface Tension: Liquid surfaces shrinking to minimum area.

Examples:
- Hydraulic lifts in car workshops.
- Spherical shape of raindrops.""",

    "thermodynamics": """The study of heat, temperature, and energy-work relations.
Points:
- First Law: Internal energy change equals heat added minus work done.
- Adiabatic Process: A process with no heat exchange with surroundings.
- Second Law: Heat cannot spontaneously flow from cold to hot.

Examples:
- Heat engines in cars.
- Cooling effect of a refrigerator.""",

    "oscillations": """To-and-fro motion of a particle about a mean position.
Points:
- SHM: Periodic motion where restoring force is proportional to displacement.
- Resonance: Large amplitude when external force matches natural frequency.

Examples:
- A simple pendulum in a clock.
- Vibrations in a tuning fork.""",

    "waves": """Energy propagation through a medium without matter transport.
Points:
- Longitudinal Waves: Particles vibrate parallel to wave direction (Sound).
- Doppler Effect: Frequency change due to source or observer motion.
- Superposition: Resultant displacement is the sum of wave displacements.

Examples:
- Sound waves in air.
- Bending of light around edges (Diffraction).""",

    # ======== CLASS 12 PHYSICS ========
    "electrostatics": """The study of stationary electric charges and their fields.
Points:
- Coulomb’s Law: Force between charges follows the inverse square law.
- Gauss’s Law: Total flux equals enclosed charge divided by permittivity.
- Capacitance: Ability to store electric charge and energy.

Examples:
- Static shock from a door handle.
- Storing energy in camera flash capacitors.""",

    "current": """The study of electric charge flow through conductors.
Points:
- Ohm’s Law: V = IR (Potential = Current x Resistance).
- Kirchhoff’s Laws: Rules for charge and energy conservation in loops.
- Drift Velocity: Average velocity of electrons under an electric field.

Examples:
- Electric circuits in household appliances.
- Measuring resistance with a Potentiometer.""",

    "magnetism": """Study of magnetic fields and their interaction with charges.
Points:
- Lorentz Force: Force on a charge in both electric and magnetic fields.
- Ampere’s Law: Relationship between current and magnetic field loops.
- Magnetic Materials: Categorized as Dia, Para, or Ferromagnetic.

Examples:
- Compass needles pointing North.
- Galvanometers detecting small currents.""",

    "induction": """Generation of electricity from magnetism and AC circuits.
Points:
- Faraday’s Law: EMF is induced when magnetic flux changes.
- Lenz’s Law: Induced current opposes the change that created it.
- RMS Value: Effective value of AC producing equivalent DC heat.

Examples:
- AC Generators in power plants.
- Transformers in the electrical grid.""",

    "optics": """The behavior and interaction of light as rays and waves.
Points:
- Total Internal Reflection: Light reflecting fully inside a denser medium.
- Huygens' Principle: Wavefronts acting as sources for secondary waves.
- Interference: Superposition of light waves creating bright/dark spots.

Examples:
- Fiber optic cables for internet.
- Rainbows and soap bubble colors.""",

    "quantum": """Physics of dual particle-wave nature and atomic models.
Points:
- Photoelectric Effect: Light striking metal to eject electrons.
- Bohr Model: Quantized electron orbits in atoms.
- De Broglie Waves: Moving particles behaving like waves.

Examples:
- Solar cells and light sensors.
- Electron microscopes.""",

    "nuclei": """The study of nuclear forces, stability, and energy.
Points:
- Mass-Energy: E = mc² (Mass defect converted to energy).
- Fission/Fusion: Splitting or joining nuclei to release energy.
- Radioactivity: Decay of unstable nuclei (Alpha, Beta, Gamma).

Examples:
- Nuclear power generation.
- Carbon dating of fossils.""",

    "semiconductors": """Physics of materials with controllable conductivity.
Points:
- P-N Junction: Base unit for diodes and transistors.
- Rectification: Converting AC to DC using diodes.
- Logic Gates: Circuits performing basic digital operations (AND, OR).

Examples:
- LED lights and screens.
- Microchips in smartphones."""
}


# ====== Telegram Handlers ======
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.strip().lower()  # normalize text
    summary = topics_dict.get(text, None)       # check if keyword exists
    if summary:
        await update.message.reply_text(summary)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Hey! Just type any Class 11-12 topic keyword and I'll give you exam-friendly summary with examples!"
    )

# ====== Main ======
if __name__ == "__main__":
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    print("Bot running…")
    app.run_polling()
