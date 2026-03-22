import os
import wikipedia
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, CommandHandler, filters, ContextTypes

# Wikipedia setup
wikipedia.set_lang("en")

# TOKEN from Railway ENV
TOKEN = os.getenv("TOKEN")

edu_keywords = [
    "physical quantities", "fundamental units", "derived units", "si units",
    "dimensional analysis", "significant figures",
    
    "distance", "displacement", "speed", "velocity", "acceleration",
    "equations of motion", "free fall",
    
    "scalar", "vector", "vector addition", "resolution of vectors",
    "projectile motion", "relative velocity",
    
    "inertia", "newton's laws of motion", "force", "friction",
    "tension", "momentum", "impulse",
    
    "work", "energy", "power", "kinetic energy", "potential energy",
    "work energy theorem", "conservation of energy",
    
    "universal law of gravitation", "gravitational field",
    "acceleration due to gravity", "escape velocity", "orbital velocity",
    
    "rigid body", "moment of inertia", "torque",
    "angular momentum", "rotational motion", "rolling motion",
    
    "simple harmonic motion", "time period", "frequency",
    "angular frequency", "oscillation",
    
    "wave motion", "wavelength", "wave speed",
    "superposition of waves", "doppler effect",
    
    "heat", "temperature", "thermodynamics",
    "first law of thermodynamics", "second law of thermodynamics",
    "isothermal process", "adiabatic process",
    
    "kinetic theory of gases", "ideal gas",
    "rms velocity", "mean free path",
    
    "elasticity", "stress", "strain", "hooke's law",
    "viscosity", "surface tension", "capillary action",

    "electric charge", "coulomb's law", "electric field",
    "electric field lines", "electric flux", "gauss law",
    
    "electric potential", "potential difference", "equipotential surface",
    "capacitance", "capacitor", "parallel plate capacitor",
    "energy stored in capacitor",
    
    "electric current", "drift velocity", "ohm's law",
    "resistance", "resistivity", "temperature dependence of resistance",
    "kirchhoff's laws", "wheatstone bridge",
    
    "magnetic field", "biot savart law", "ampere's law",
    "lorentz force", "force on current carrying conductor",
    "moving coil galvanometer",
    
    "electromagnetic induction", "faraday's law", "lenz law",
    "self induction", "mutual induction",
    
    "alternating current", "rms value", "reactance",
    "impedance", "power factor", "lc oscillations",
    
    "electromagnetic waves", "spectrum of electromagnetic waves",
    
    "ray optics", "reflection", "refraction", "snell's law",
    "total internal reflection", "mirror formula", "lens formula",
    "magnification",
    
    "wave optics", "interference", "young's double slit experiment",
    "diffraction", "polarization",
    
    "dual nature of matter", "photoelectric effect",
    "de broglie wavelength",
    
    "atoms", "bohr model", "energy levels",
    
    "nuclei", "radioactivity", "half life",
    "nuclear fission", "nuclear fusion",
    
    "semiconductors", "p type semiconductor", "n type semiconductor",
    "pn junction", "diode", "transistor",
    
    "logic gates", "and gate", "or gate", "not gate",

    "sets", "subset", "superset", "union of sets", "intersection of sets",
    "complement of sets", "venn diagram",
    
    "relations", "functions", "domain", "range", "codomain",
    "one one function", "onto function",
    
    "trigonometric functions", "trigonometric identities",
    "sine", "cosine", "tangent",
    "trigonometric equations",
    
    "complex numbers", "imaginary numbers", "modulus", "argument",
    
    "linear inequalities", "solution of inequalities",
    
    "permutations", "combinations", "factorial",
    
    "binomial theorem", "binomial expansion",
    
    "sequence", "series", "arithmetic progression",
    "geometric progression", "sum of n terms",
    
    "straight lines", "slope", "intercept",
    "equation of line", "distance between two points",
    "section formula",
    
    "conic sections", "circle", "parabola",
    "ellipse", "hyperbola",
    
    "limits", "derivatives", "continuity",
    
    "statistics", "mean", "median", "mode",
    "standard deviation", "variance",
    
    "probability", "random experiment",
    "sample space", "event",

    "relations and functions", "types of relations", "types of functions",
    "domain", "range", "one one function", "onto function", "inverse function",
    
    "matrices", "types of matrices", "transpose of matrix",
    "determinant", "properties of determinants", "adjoint of matrix",
    "inverse of matrix",
    
    "continuity", "differentiability", "derivative",
    "chain rule", "product rule", "quotient rule",
    
    "application of derivatives", "increasing and decreasing functions",
    "maxima and minima", "tangent and normal",
    
    "integrals", "indefinite integrals", "definite integrals",
    "integration by substitution", "integration by parts",
    "area under curve",
    
    "differential equations", "order of differential equation",
    "degree of differential equation", "solution of differential equation",
    
    "vector algebra", "vector addition", "dot product",
    "cross product", "scalar triple product",
    
    "three dimensional geometry", "direction cosines",
    "direction ratios", "equation of line in space",
    "shortest distance between lines",
    
    "linear programming", "feasible region",
    "optimal solution",
    
    "probability", "conditional probability",
    "bayes theorem", "random variable",
    "probability distribution", "mean of distribution",
    "variance of distribution",

     "some basic concepts of chemistry", "mole concept", "stoichiometry",
    "law of conservation of mass", "law of definite proportions",
    
    "atomic structure", "bohr model", "quantum numbers",
    "electronic configuration", "orbitals",
    
    "periodic classification", "modern periodic law",
    "periodic trends", "atomic radius", "ionization energy",
    "electron affinity", "electronegativity",
    
    "chemical bonding", "ionic bond", "covalent bond",
    "polar covalent bond", "valence bond theory",
    "hybridization", "vsepr theory", "molecular geometry",
    
    "states of matter", "gas laws", "boyle's law",
    "charles law", "ideal gas equation", "kinetic theory of gases",
    
    "thermodynamics", "system and surroundings",
    "internal energy", "enthalpy", "entropy",
    "gibbs free energy",
    
    "equilibrium", "chemical equilibrium",
    "dynamic equilibrium", "le chatelier principle",
    "equilibrium constant",
    
    "redox reactions", "oxidation", "reduction",
    "oxidizing agent", "reducing agent",
    
    "hydrogen", "properties of hydrogen",
    
    "s block elements", "alkali metals", "alkaline earth metals",
    
    "p block elements", "group 13 elements", "group 14 elements",
    
    "organic chemistry basics", "hydrocarbons",
    "alkanes", "alkenes", "alkynes",
    "isomerism", "functional groups",
    
    "environmental chemistry", "air pollution",
    "water pollution", "greenhouse effect",

     "solid state", "crystal lattice", "unit cell",
    "packing efficiency", "density of unit cell",
    
    "solutions", "molarity", "molality", "normality",
    "raoult's law", "colligative properties",
    "osmotic pressure",
    
    "electrochemistry", "electrolyte", "conductance",
    "kohlrausch law", "electrochemical cell",
    "nernst equation",
    
    "chemical kinetics", "rate of reaction",
    "rate law", "order of reaction",
    "activation energy", "arrhenius equation",
    
    "surface chemistry", "adsorption", "absorption",
    "catalysis", "colloids",
    
    "general principles of metallurgy", "concentration of ores",
    "calcination", "roasting", "refining",
    
    "p block elements", "group 15 elements",
    "group 16 elements", "group 17 elements",
    "group 18 elements",
    
    "d and f block elements", "transition elements",
    "lanthanides", "actinides",
    
    "coordination compounds", "ligands",
    "coordination number", "isomerism in coordination compounds",
    
    "haloalkanes", "haloarenes",
    "nucleophilic substitution",
    
    "alcohols", "phenols", "ethers",
    "acidic nature of alcohols",
    
    "aldehydes", "ketones", "carboxylic acids",
    "oxidation reactions", "reduction reactions",
    
    "amines", "basicity of amines",
    
    "biomolecules", "carbohydrates", "proteins",
    "enzymes", "vitamins",
    
    "polymers", "addition polymerization",
    "condensation polymerization",
    
    "chemistry in everyday life", "drugs",
    "antiseptics", "disinfectants",

    # Class 11 Biology
    "living world", "biodiversity", "taxonomy", "binomial nomenclature",
    
    "biological classification", "five kingdom classification",
    "monera", "protista", "fungi", "plantae", "animalia",
    
    "plant kingdom", "algae", "bryophytes", "pteridophytes",
    "gymnosperms", "angiosperms",
    
    "animal kingdom", "invertebrates", "vertebrates",
    
    "morphology of flowering plants", "root", "stem", "leaf",
    "flower", "inflorescence", "fruit", "seed",
    
    "anatomy of flowering plants", "tissues", "xylem", "phloem",
    
    "structural organisation in animals", "animal tissues",
    
    "cell", "cell theory", "prokaryotic cell", "eukaryotic cell",
    "cell organelles", "nucleus", "mitochondria", "ribosome",
    
    "biomolecules", "carbohydrates", "proteins", "lipids",
    "enzymes", "nucleic acids",
    
    "cell cycle", "mitosis", "meiosis",
    
    "transport in plants", "diffusion", "osmosis", "active transport",
    "transpiration",
    
    "mineral nutrition", "macronutrients", "micronutrients",
    
    "photosynthesis", "light reaction", "dark reaction",
    
    "respiration in plants", "glycolysis", "krebs cycle",
    
    "plant growth and development", "plant hormones",
    "auxins", "gibberellins", "cytokinins",
    
    # Class 12 Biology
    "reproduction in organisms", "asexual reproduction",
    "sexual reproduction",
    
    "human reproduction", "male reproductive system",
    "female reproductive system", "menstrual cycle",
    
    "reproductive health", "contraception", "fertility",
    
    "principles of inheritance", "mendel laws",
    "dominant traits", "recessive traits",
    
    "molecular basis of inheritance", "dna", "rna",
    "replication", "transcription", "translation",
    
    "evolution", "natural selection", "darwin theory",
    
    "human health and disease", "pathogens", "immunity",
    "vaccination", "antibodies",
    
    "microbes in human welfare", "fermentation",
    "antibiotics",
    
    "biotechnology", "genetic engineering",
    "recombinant dna technology",
    
    "organisms and populations", "ecosystem",
    "food chain", "food web",
    
    "biodiversity and conservation",
    "environmental issues", "pollution",
    "global warming"
]
async def edu_wiki_bot(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not update.message or not update.message.text:
        return

    message_text = update.message.text.lower().strip()
    print("Message:", message_text)

    for keyword in sorted(edu_keywords, key=len, reverse=True):
        if keyword in message_text:
            try:
                summary = wikipedia.summary(keyword, sentences=2)
                await update.message.reply_text(f"📚 {keyword.title()}:\n{summary}")
                return
            except wikipedia.exceptions.DisambiguationError as e:
                await update.message.reply_text(
                    f"Multiple results for {keyword}:\n{', '.join(e.options[:5])}"
                )
                return
            except wikipedia.exceptions.PageError:
                await update.message.reply_text(f"❌ No page found for {keyword}")
                return
            except Exception as e:
                await update.message.reply_text("⚠️ Error fetching data")
                print(e)
                return

# /say command
async def say(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if context.args:
        await update.message.reply_text(" ".join(context.args))
    else:
        await update.message.reply_text("❌ Use like: /say hello")

# START BOT
app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), edu_wiki_bot))
app.add_handler(CommandHandler("say", say))

print("✅ Bot is running...")
app.run_polling(close_loop=False)
