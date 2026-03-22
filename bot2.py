from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes
import wikipedia

TOKEN = "8784516259:AAE2030kvj3TUI24myprFXSbJG8lDzDZYqs"

edu_keywords = [
    # Physics – Class 11
    "motion", "laws of motion", "rotation", "work", "energy", "power",
    "gravitation", "oscillation", "waves", "current electricity",
    "ohm's law", "magnetism", "momentum", "impulse", "torque",
    
    # Physics – Class 12
    "electromagnetic induction", "alternating current", "optics", "refraction", "lens", 
    "mirrors", "wave optics", "thermodynamics", "kinetic theory", "oscillations",
    
    # Chemistry – Class 11
    "atomic structure", "periodic table", "chemical bonding", "ionic bond", "covalent bond",
    "stoichiometry", "mole concept", "electrochemistry", "thermodynamics", "states of matter",
    
    # Chemistry – Class 12
    "equilibrium", "acid base", "buffer solution", "solubility product", "electrochemistry",
    "coordination compounds", "surface chemistry", "chemical kinetics", "thermodynamics", "nuclear chemistry",
    
    # Maths – Class 11
    "limits", "derivatives", "integration", "vectors", "matrices", "determinants",
    "probability", "sequence", "series", "coordinate geometry",
    
    # Maths – Class 12
    "continuity", "differentiability", "application of derivatives", "integration methods",
    "definite integrals", "differential equations", "three dimensional geometry",
    "linear programming", "relations and functions", "matrices and determinants"
]

async def edu_wiki_bot(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_text = update.message.text.lower().strip()
    if not message_text:
        return

    # Check if message contains any educational keyword
    for keyword in edu_keywords:
        if keyword in message_text:
            try:
                summary = wikipedia.summary(keyword, sentences=3)
                await update.message.reply_text(f"📚 {keyword.title()} Summary:\n{summary}")
                return  # reply only once per message
            except wikipedia.exceptions.DisambiguationError as e:
                await update.message.reply_text(f"Multiple options found for {keyword}. Did you mean: {', '.join(e.options[:5])}?")
                return
            except wikipedia.exceptions.PageError:
                await update.message.reply_text(f"Sorry, couldn't find a page for {keyword}.")
                return

# Set up bot
app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), edu_wiki_bot))

print("Bot is running...")
app.run_polling()
