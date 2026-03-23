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

    # ======== CLASS 11 CHEMISTRY ========
    "basic concepts": """The foundation of chemistry involving the study of matter and its measurements.
Points:
- Mole Concept: One mole contains exactly 6.022 x 10^23 particles (Avogadro's number).
- Stoichiometry: Calculating the amounts of reactants and products in a chemical reaction.
- Empirical Formula: The simplest whole-number ratio of atoms in a compound.

Examples:
- Calculating the amount of CO2 produced when burning methane.
- Determining the molarity of a salt solution.""",

    "atom structure": """The study of subatomic particles and the arrangement of electrons in an atom.
Points:
- Quantum Numbers: Set of four numbers used to describe the position and energy of electrons.
- Heisenberg Principle: It is impossible to determine both position and momentum of an electron simultaneously.
- Aufbau Principle: Electrons fill lower energy orbitals before higher ones.

Examples:
- Writing the electronic configuration of Chromium (Cr).
- Identifying elements based on their unique emission spectra.""",

    "periodic table": """Classification of elements and the study of recurring chemical trends.
Points:
- Ionization Enthalpy: Energy required to remove an electron from a gaseous atom.
- Electronegativity: The tendency of an atom to attract shared electrons in a bond.
- Periodic Trends: Metallic character decreases and non-metallic character increases across a period.

Examples:
- Explaining why Fluorine is more reactive than Iodine.
- Predicting the chemical properties of an unknown element.""",

    "chemical bonding": """The study of forces that hold atoms together in molecules.
Points:
- VSEPR Theory: Predicts the 3D shape of molecules based on electron pair repulsion.
- Hybridization: Mixing of atomic orbitals to form new equivalent hybrid orbitals (sp, sp2, sp3).
- Hydrogen Bonding: Strong dipole-dipole attraction involving Hydrogen and F, O, or N.

Examples:
- Why water (H2O) has a bent shape.
- The high boiling point of water compared to H2S.""",

    "chem thermodynamics": """Study of energy changes, heat transfer, and spontaneity of reactions.
Points:
- Enthalpy (H): Total heat content of a system at constant pressure.
- Gibbs Free Energy (G): Determines if a reaction is spontaneous (ΔG < 0).
- Entropy (S): The measure of randomness or disorder in a system.

Examples:
- Calculating heat released during the combustion of fuels.
- Predicting if ice will melt at a specific temperature.""",

    "equilibrium": """The state where the rates of forward and reverse reactions are equal.
Points:
- Le Chatelier’s Principle: If a system at equilibrium is disturbed, it shifts to counteract the change.
- pH Scale: A measure of the acidity or basicity of an aqueous solution.
- Solubility Product (Ksp): Equilibrium between a solid and its ions in a saturated solution.

Examples:
- The Haber process for ammonia production.
- How buffers in human blood maintain a constant pH.""",

    "redox": """Reactions involving the transfer of electrons between species.
Points:
- Oxidation State: The formal charge an atom would have if all bonds were ionic.
- Half-Reaction Method: Balancing equations by separating oxidation and reduction steps.
- Oxidizing Agent: A substance that gains electrons and gets reduced.

Examples:
- Rusting of iron in the presence of moisture.
- Chemical reactions inside a common AA battery.""",

    "organic basics": """Introduction to carbon compounds and their nomenclature/mechanisms.
Points:
- IUPAC Nomenclature: Systematic naming of organic compounds.
- Isomerism: Compounds with the same formula but different structures.
- Inductive Effect: Permanent displacement of electrons along a carbon chain.

Examples:
- Distinguishing between Pentane and Isopentane.
- Explaining why certain molecules are more acidic than others.""",

    "hydrocarbons": """Study of Alkanes, Alkenes, and Alkynes.
Points:
- Substitution Reactions: Characteristic of saturated hydrocarbons (Alkanes).
- Addition Reactions: Characteristic of unsaturated hydrocarbons (Alkenes/Alkynes).
- Resonance in Benzene: The stability of aromatic rings due to delocalized pi-electrons.

Examples:
- Production of polymers like Polythene from Ethene.
- Chlorination of methane under sunlight.""",

    # ======== CLASS 12 CHEMISTRY ========
    "solutions": """The study of homogeneous mixtures and their physical properties.
Points:
- Raoult’s Law: Vapor pressure of a solution is proportional to the mole fraction of the solvent.
- Colligative Properties: Properties like boiling point elevation that depend only on particle count.
- Henry’s Law: Gas solubility in a liquid is proportional to its partial pressure.

Examples:
- Adding salt to water to make it boil at a higher temperature.
- Carbon dioxide dissolving in soda under high pressure.""",

    "electrochemistry": """The relationship between chemical energy and electrical energy.
Points:
- Nernst Equation: Calculates cell potential under non-standard conditions.
- Electrolysis: Using electricity to drive a non-spontaneous chemical change.
- Kohlrausch's Law: Limiting molar conductivity of an electrolyte.

Examples:
- Gold plating jewelry using electrolysis.
- Rechargeable Lithium-ion batteries in phones.""",

    "chemical kinetics": """The study of reaction rates and their mechanisms.
Points:
- Order of Reaction: The power to which a reactant's concentration is raised in the rate law.
- Activation Energy: The minimum energy required to initiate a chemical reaction.
- Catalysis: Increasing reaction speed by lowering the activation energy barrier.

Examples:
- How enzymes speed up digestion.
- Calculating the shelf-life of medicines.""",

    "d-f block": """The study of transition and inner-transition elements.
Points:
- Variable Oxidation States: Transition metals can lose different numbers of electrons.
- Lanthanoid Contraction: The steady decrease in atomic size across the 4f series.
- Coordination Compounds: Molecules where a central metal atom is bonded to ligands.

Examples:
- Iron being used as a catalyst in industrial processes.
- The use of Hemoglobin (Iron complex) in carrying oxygen.""",

    "haloalkanes": """Organic compounds containing halogen atoms attached to carbon.
Points:
- Nucleophilic Substitution (SN1/SN2): Mechanisms for replacing halogens with other groups.
- Optical Activity: The ability of chiral molecules to rotate plane-polarized light.

Examples:
- Use of Chloroform as an early anesthetic.
- Production of Teflon from halogenated monomers.""",

    "alcohols phenols": """Compounds containing the -OH (hydroxyl) group.
Points:
- Acidity of Phenol: Phenols are more acidic than alcohols due to resonance stabilization.
- Dehydration: Converting alcohols into alkenes using acid catalysts.

Examples:
- Ethanol used as a fuel additive and antiseptic.
- Synthesis of Aspirin from Salicylic acid.""",

    "carbonyls": """The chemistry of Aldehydes, Ketones, and Carboxylic Acids.
Points:
- Nucleophilic Addition: The primary reaction type for the C=O functional group.
- Aldol Condensation: Reaction between carbonyls containing alpha-hydrogen.

Examples:
- Formaldehyde used in preserving biological specimens.
- Acetic acid being the main component of vinegar.""",

    "amines": """Organic derivatives of ammonia containing Nitrogen.
Points:
- Basicity: Amines act as bases due to the lone pair on the Nitrogen atom.
- Diazotization: Converting primary aromatic amines into diazonium salts.

Examples:
- Synthesis of colorful azo-dyes.
- Adrenaline acting as a chemical messenger in the body.""",

    "biomolecules": """The chemical basis of living organisms.
Points:
- Carbohydrates: Source of energy (Glucose, Starch, Cellulose).
- Proteins: Polymers of amino acids linked by peptide bonds.
- DNA/RNA: Nucleic acids that store and transmit genetic information.

Examples:
- Denaturation of egg whites when cooked.
- DNA profiling used in forensic science."""


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
