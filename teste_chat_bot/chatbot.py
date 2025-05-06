import gradio as gr

dados_usuario = {}

mensagem_inicial = [("🤖 PetCareBot", "Olá! Bem-vindo à Clínica PetCare 🐾\nComo posso te chamar?")]

def atendimento(mensagem, historico):
    global dados_usuario

    if not mensagem or not isinstance(mensagem, str):
        resposta = "Desculpe, não entendi. Pode repetir?"
        historico.append(("", resposta))
        return "", historico

    if not historico or len(historico) <= 1:
        historico = mensagem_inicial.copy()

    # Etapa 1: Nome do tutor
    if "nome_tutor" not in dados_usuario:
        dados_usuario["nome_tutor"] = mensagem.strip().capitalize()
        resposta = f"Prazer, {dados_usuario['nome_tutor']}! Qual é o nome do seu pet?"
        historico.append((mensagem, resposta))
        return "", historico

    # Etapa 2: Nome do pet
    if "nome_pet" not in dados_usuario:
        dados_usuario["nome_pet"] = mensagem.strip().capitalize()
        resposta = f"Legal! O {dados_usuario['nome_pet']} é um cachorro, gato ou outro?"
        historico.append((mensagem, resposta))
        return "", historico

    # Etapa 3: Tipo de pet
    if "tipo_pet" not in dados_usuario:
        dados_usuario["tipo_pet"] = mensagem.strip().capitalize()
        resposta = "Certo. Qual serviço deseja agendar?\n- Consulta\n- Exame\n- Castração"
        historico.append((mensagem, resposta))
        return "", historico

    # Etapa 4: Serviço
    if "servico" not in dados_usuario:
        servico = mensagem.lower()
        if servico not in ["consulta", "exame", "castração", "castracao"]:
            resposta = "Serviço não reconhecido. Por favor, escolha entre: Consulta, Exame ou Castração."
        else:
            dados_usuario["servico"] = "castração" if servico == "castracao" else servico
            resposta = f"Perfeito. Para qual dia deseja agendar o serviço de {dados_usuario['servico']}?"
        historico.append((mensagem, resposta))
        return "", historico

    # Etapa 5: Data
    if "data" not in dados_usuario:
        dados_usuario["data"] = mensagem.strip()
        resposta = (
            f"✅ Agendamento confirmado!\n\n"
            f"Tutor: {dados_usuario['nome_tutor']}\n"
            f"Pet: {dados_usuario['nome_pet']} ({dados_usuario['tipo_pet']})\n"
            f"Serviço: {dados_usuario['servico'].capitalize()}\n"
            f"Data: {dados_usuario['data']}\n\n"
            f"Nos vemos em breve! 🐶🐱"
        )
        historico.append((mensagem, resposta))
        dados_usuario = {}  # Reset
        return "", historico

with gr.Blocks() as demo:
    gr.Markdown("## 💬 Chat de Agendamento - Clínica PetCare")
    chatbot = gr.Chatbot(value=mensagem_inicial, height=400)
    msg = gr.Textbox(placeholder="Digite sua resposta aqui...", label="Sua mensagem")
    state = gr.State(mensagem_inicial)

    def responder(mensagem, chat_state):
        return atendimento(mensagem, chat_state)

    msg.submit(responder, [msg, state], [msg, chatbot, state])

demo.launch(share=True)
