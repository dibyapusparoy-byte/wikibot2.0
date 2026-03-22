TOKEN = os.getenv("BOT_TOKEN")  # safer for deploy

edu_keywords = [
    "motion", "laws of motion", "rotation", "work", "energy", "power",
    "gravitation", "oscillation", "waves", "current electricity",
    "ohm's law", "magnetism", "momentum", "impulse", "torque",
    "electromagnetic induction", "alternating current", "optics", "refraction", "lens", 
    "mirrors", "wave optics", "thermodynamics", "kinetic theory", "oscillations",
    "atomic structure", "periodic table", "chemical bonding", "ionic bond", "covalent bond",
    "stoichiometry", "mole concept", "electrochemistry", "states of matter",
    "equilibrium", "acid base", "buffer solution", "solubility product",
    "coordination compounds", "surface chemistry", "chemical kinetics", "nuclear chemistry",
    "limits", "derivatives", "integration", "vectors", "matrices", "determinants",
    "probability", "sequence", "series", "coordinate geometry",
    "continuity", "differentiability", "application of derivatives", "integration methods",
    "definite integrals", "differential equations", "three dimensional geometry",
    "linear programming", "relations and functions"
]

def format_summary(keyword, summary):
    return (
        f"📚 *{keyword.upper()}*\n\n"
        f"🧠 *Concept:*\n{summary}\n\n"
        f"✨ _Quick Tip: Revise this topic for JEE/Boards 💯_"
    )

async def edu_wiki_bot(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_text = update.message.text.lower().strip()
    if not message_text:
        return

    for keyword in edu_keywords:
        if keyword in message_text:
            try:
                summary = wikipedia.summary(keyword, sentences=3)
                
                beautified_text = format_summary(keyword, summary)

                await update.message.reply_text(
                    beautified_text,
                    parse_mode="Markdown"
                )
                return

            except wikipedia.exceptions.DisambiguationError as e:
                await update.message.reply_text(
                    f"⚠️ *Multiple results found!*\n\nDid you mean:\n👉 {', '.join(e.options[:5])}",
                    parse_mode="Markdown"
                )
                return

            except wikipedia.exceptions.PageError:
                await update.message.reply_text(
                    f"❌ *No data found* for *{keyword}*",
                    parse_mode="Markdown"
                )
                return

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), edu_wiki_bot))

print("Bot is running...")
app.run_polling()
