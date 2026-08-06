from gem import chat
from i18n import t, TRANSLATIONS

ANSWER_PROMPT = """You answer questions about a bank loan's Terms & Conditions.
Use ONLY the context below. Do not use outside knowledge.

If the answer is NOT clearly in the context, reply exactly:
"{not_stated}"

When you do answer, quote the exact number / fee / rule and add the page, e.g. (p. 3).

IMPORTANT: You must write your final answer entirely in the {language_name} language.

Context:
{context}

Question: {q}
Answer:"""

def write_answer(question, chunks, lang="EN"):
    context = "\n\n".join(f"[p. {c['page']}] {c['text']}" for c in chunks)
    not_stated = t("not_stated", lang)
    language_name = TRANSLATIONS.get("lang_" + lang.lower(), {}).get(lang, "English")
    
    return chat(ANSWER_PROMPT.format(
        not_stated=not_stated,
        language_name=language_name,
        context=context, 
        q=question
    ))

