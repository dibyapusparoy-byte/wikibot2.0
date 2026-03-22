# filename: class11_12_bot_dict_only.py
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

# ====== CONFIG ======
TOKEN = "8784516259:AAE2030kvj3TUI24myprFXSbJG8lDzDZYqs"  # Telegram bot token

# ====== Predefined Class 11-12 Topics with 4-5 line definitions + examples ======
topics_dict = {
    # ======== CLASS 11 PHYSICS ========
    "motion": "Motion describes the change in position of an object with time. It can be uniform (constant speed) or non-uniform (changing speed).\nExamples:\n- A car moving on a highway (uniform motion)\n- A ball rolling down a slope (non-uniform motion)",

    "laws of motion": "Newton's laws explain how forces affect motion:\n1st Law: A body remains at rest or in uniform motion unless acted upon by a force.\n2nd Law: Force = Mass x Acceleration.\n3rd Law: For every action, there is an equal and opposite reaction.\nExamples:\n- Rocket launch (3rd law)\n- Car braking suddenly (2nd law)\n- Ball stays still on table until pushed (1st law)",

    "rotation": "Rotation is the circular movement of an object around a fixed axis.\nExamples:\n- Earth spinning around its axis\n- Bicycle wheel spinning",

    "work": "Work is done when a force moves an object through a distance in the direction of force.\nExamples:\n- Lifting a book\n- Pushing a cart",

    "energy": "Energy is the capacity to do work. Forms include kinetic energy (motion) and potential energy (position).\nExamples:\n- Moving car (kinetic)\n- Stretched rubber band (potential)",

    "gravitation": "Gravitation is the force of attraction between any two masses.\nExamples:\n- Objects falling to the ground\n- Earth attracting the Moon",

    "oscillations": "Oscillations are repeated back-and-forth motions around an equilibrium point.\nExamples:\n- Pendulum of a clock\n- Vibrating guitar string",

    "waves": "Waves are disturbances that transfer energy without transferring matter.\nExamples:\n- Sound waves\n- Water waves in a pond",

    "thermodynamics": "Thermodynamics deals with heat, work, and energy transfer.\nExamples:\n- Steam engine converting heat to work\n- Refrigerators transferring heat from cold to hot region",

    "optics": "Optics is the study of light, reflection, refraction, and optical instruments.\nExamples:\n- Lenses in spectacles\n- Mirrors in periscopes",

    "electrostatics": "Electrostatics studies charges at rest and forces between them.\nExamples:\n- Rubbing a balloon and sticking it on wall\n- Lightning",

    "current electricity": "Current electricity deals with the flow of charges in a conductor.\nExamples:\n- Electric circuits\n- Charging a mobile phone",

    "magnetism": "Magnetism studies magnetic fields and forces between magnets.\nExamples:\n- Compass needle pointing North\n- Electric motors",

    "modern physics": "Modern physics includes concepts like photoelectric effect, atomic models, and nuclear physics.\nExamples:\n- Solar cells (photoelectric effect)\n- Nuclear reactors (nuclear fission)",

    # ======== CLASS 11 CHEMISTRY ========
    "structure of atom": "Atoms have electrons, protons, and neutrons arranged in shells and energy levels.\nExamples:\n- Hydrogen atom: 1 proton, 1 electron\n- Sodium atom: electron configuration 2,8,1",

    "periodic table": "Elements arranged by atomic number showing recurring properties.\nExamples:\n- Group 1: Alkali metals\n- Group 17: Halogens",

    "chemical bonding": "Atoms form bonds to achieve stability: ionic, covalent, and metallic.\nExamples:\n- NaCl (ionic)\n- H2O (covalent)\n- Cu wire (metallic)",

    "thermodynamics": "Study of heat and energy changes in chemical reactions.\nExamples:\n- Combustion of fuels\n- Dissolving salts in water (endothermic/exothermic)",

    "equilibrium": "Chemical equilibrium occurs when rates of forward and reverse reactions are equal.\nExamples:\n- Haber process (NH3 formation)\n- Dissolving CO2 in soda",

    "redox reactions": "Redox reactions involve transfer of electrons: oxidation and reduction.\nExamples:\n- Rusting of iron\n- Batteries generating electricity",

    "hydrogen": "Hydrogen properties and compounds.\nExamples:\n- H2 as fuel\n- Water formation H2 + O2 → H2O",

    "s-block elements": "Alkali and alkaline earth metals.\nExamples:\n- Na, K (reactive metals)\n- Ca, Mg in bones and teeth",

    "p-block elements": "Groups 13-18 elements with distinct chemistry.\nExamples:\n- Boron, Aluminium (metalloids)\n- Halogens, Noble gases",

    "organic chemistry basics": "Study of carbon compounds.\nExamples:\n- Methane (CH4)\n- Ethanol (C2H5OH)",

    # ======== CLASS 11 MATHS ========
    "sets": "A set is a collection of distinct objects.\nExamples:\n- {1,2,3}\n- {students in a class}",

    "relations and functions": "Relation: mapping between sets. Function: each input has one output.\nExamples:\n- f(x) = x^2\n- y = sin(x)",

    "algebra": "Study of polynomials, quadratic equations, sequences, etc.\nExamples:\n- Solving x^2 - 5x + 6 = 0\n- Arithmetic progression: 2,5,8,11,...",

    "calculus": "Limits, derivatives, and integrals of functions.\nExamples:\n- Rate of change of distance (derivative)\n- Area under curve (integral)",

    "coordinate geometry": "Study of points, lines, curves in 2D/3D space.\nExamples:\n- Distance formula\n- Equation of line y = mx + c",

    "vectors": "Quantities having magnitude and direction.\nExamples:\n- Velocity vector\n- Force vector",

    "probability": "Measure of likelihood of events.\nExamples:\n- Tossing a coin: P(head) = 1/2\n- Rolling a dice: P(6) = 1/6",

    # ======== CLASS 12 PHYSICS ========
    "electromagnetic induction": "Changing magnetic field induces current in a conductor.\nExamples:\n- Electric generator\n- Induction stove",

    "alternating current": "Current changing direction periodically.\nExamples:\n- Household AC\n- Transformers",

    "electromagnetic waves": "Oscillating electric and magnetic fields propagate through space.\nExamples:\n- Radio waves\n- Light waves",

    "semiconductors": "Materials with conductivity between conductors and insulators.\nExamples:\n- Silicon, Germanium\n- Diodes and transistors",

    "communication systems": "Transmission of information using signals.\nExamples:\n- Internet, Mobile phones\n- Satellite communication",

    # ======== CLASS 12 CHEMISTRY ========
    "solid state": "Study of structure, properties of solids.\nExamples:\n- Crystalline: NaCl\n- Amorphous: Glass",

    "solutions": "Homogeneous mixtures of solute and solvent.\nExamples:\n- Sugar in water\n- Saltwater",

    "electrochemistry": "Chemical reactions producing electricity or using electricity.\nExamples:\n- Galvanic cells\n- Electroplating",

    "chemical kinetics": "Study of reaction rates.\nExamples:\n- Rusting speed\n- Decomposition of H2O2",

    "surface chemistry": "Phenomena at surfaces and interfaces.\nExamples:\n- Detergent action\n- Catalysis",

    "organic chemistry advanced": "Includes carbonyl compounds, alcohols, amines, polymers.\nExamples:\n- Ethanol, Acetone\n- Nylon, Teflon",

    # ======== CLASS 12 MATHS ========
    "matrices": "Rectangular arrays of numbers.\nExamples:\n- [[1,2],[3,4]]\n- Transformation matrices in graphics",

    "determinants": "Special number from square matrix used to solve systems.\nExamples:\n- Solving 2x2 linear equations\n- Area of triangle using coordinates",

    "continuity and differentiability": "Study of smoothness and slope of functions.\nExamples:\n- Checking if f(x)=x^2 is continuous\n- Derivative of sin(x) is cos(x)",

    "applications of derivatives": "Derivatives applied to max/min problems, motion, etc.\nExamples:\n- Maximizing area\n- Speed and acceleration of moving objects",

    "integrals": "Inverse of derivatives; area under curves.\nExamples:\n- Area between curves\n- Total distance from velocity-time graph",

    "vectors 3D": "Vectors in three-dimensional space.\nExamples:\n- Position vector of a point in 3D\n- Force in 3D space",

    "probability advanced": "Conditional probability, distributions.\nExamples:\n- Probability of drawing red ball given first ball was green\n- Binomial distribution in experiments"
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
