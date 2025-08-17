// TraduzAI - Adobe Illustrator Text Variables Automation
// Created by Wedny Fernandes - https://wednyfernandes.com.br
// Version 1.0.0 - Brazilian Design Automation

// =============================================================================
// CONFIGURAÇÕES - ALTERE CONFORME SUA LINGUAGEM E CONFIGURAÇÃO
// =============================================================================

// Nome da ação que você criou para converter texto em variável
var ACTION_NAME = "setvar";

// Nome do conjunto de ações onde sua ação está localizada
var ACTION_SET = "Ações Padrão"; // Português: "Ações Padrão" | English: "Default Actions" | etc.

// Prefixo para nomes das variáveis no CSV (será numerado automaticamente)
var VARIABLE_PREFIX = "Variável"; // Português: "Variável" | English: "Variable" | etc.

// =============================================================================
// INSTRUÇÕES PARA CONFIGURAÇÃO:
// - ACTION_NAME: Nome exato da ação que você criou
// - ACTION_SET: Nome do conjunto onde está a ação (varia por idioma)
// - VARIABLE_PREFIX: Como nomear as colunas no CSV
//
// Exemplos por idioma:
// Português BR: ACTION_SET = "Ações Padrão"
// English: ACTION_SET = "Default Actions" 
// Español: ACTION_SET = "Acciones por defecto"
// Français: ACTION_SET = "Actions par défaut"
// =============================================================================

// ===============================
// INTERFACE SCRIPTUI
// ===============================
var win = new Window('dialog', 'TraduzAI - Wedny Fernandes');
win.orientation = 'column';
win.alignChildren = ['center', 'top'];
win.spacing = 15;

// Barra de progresso
var progressBar = win.add('progressbar', undefined, 0, 100);
progressBar.preferredSize.width = 350;
var progressText = win.add('statictext', undefined, 'Aguardando início...');
progressText.alignment = 'center';

// Botão Start (maior e azul)
var startBtn = win.add('button', undefined, 'START');
startBtn.preferredSize.width = 200;
startBtn.preferredSize.height = 40;
startBtn.fillBrush = startBtn.graphics.newBrush(startBtn.graphics.BrushType.SOLID_COLOR, [0.2, 0.4, 0.8, 1]);

// Botão cancelar
var cancelBtn = win.add('button', undefined, 'Cancelar');
cancelBtn.preferredSize.width = 120;
cancelBtn.enabled = false;

// Botão para exportar CSV das variáveis existentes
var exportBtn = win.add('button', undefined, 'Exportar CSV Existente');
exportBtn.preferredSize.width = 180;
exportBtn.alignment = 'center';

// Toggle para backup
var backupGroup = win.add('group');
backupGroup.orientation = 'row';
backupGroup.alignment = 'center';
var backupCheckbox = backupGroup.add('checkbox', undefined, 'Criar backup automático');
backupCheckbox.value = true;

// Separador
var separator = win.add('panel');
separator.preferredSize.height = 2;

// Campos editáveis (seção configurações)
var configTitle = win.add('statictext', undefined, 'Configurações Avançadas');
configTitle.alignment = 'center';

var actionNameGroup = win.add('group');
actionNameGroup.add('statictext', undefined, 'Action Name:');
var actionNameField = actionNameGroup.add('edittext', undefined, ACTION_NAME);
actionNameField.characters = 20;

var actionSetGroup = win.add('group');
actionSetGroup.add('statictext', undefined, 'Action Set:');
var actionSetField = actionSetGroup.add('edittext', undefined, ACTION_SET);
actionSetField.characters = 20;

var variablePrefixGroup = win.add('group');
variablePrefixGroup.add('statictext', undefined, 'Variable Prefix:');
var variablePrefixField = variablePrefixGroup.add('edittext', undefined, VARIABLE_PREFIX);
variablePrefixField.characters = 20;

// Separador
var separator2 = win.add('panel');
separator2.preferredSize.height = 2;

// Créditos (no final)
var credits = win.add('statictext', undefined, 'Desenvolvido por Wedny Fernandes - wednyfernandes.com.br');
credits.alignment = 'center';
credits.graphics.font = ScriptUI.newFont('dialog', 'ITALIC', 10);

// Variável de controle de cancelamento
var cancelRequested = false;

// Função para atualizar progresso
function updateProgress(current, total) {
    progressBar.value = Math.round((current / total) * 100);
    progressText.text = 'Processando ' + current + ' de ' + total + '...';
}

// Função principal de processamento (em lotes) - OTIMIZADA COM PROTEÇÃO ANTI-TRAVAMENTO
function processSelectionAsync(sel, batchSize) {
    var total = sel.length;
    var i = 0;
    var variablesData = [];
    var processStartTime = new Date().getTime();
    var maxProcessingTime = 600000; // 10 minutos máximo (aumentado de 5)
    cancelRequested = false;
    
    // Limite de objetos para evitar travamento - MAIS RESTRITIVO
    if (total > 50) {
        if (!confirm("Você selecionou " + total + " objetos. Para máquinas fracas, o limite recomendado é 50 objetos.\n\nProcessar muitos objetos pode causar travamento. Continuar?")) {
            startBtn.enabled = true;
            return;
        }
    }
    
    // Aviso adicional para muitos objetos
    if (total > 100) {
        if (!confirm("ATENÇÃO: " + total + " objetos é um número muito alto!\n\nRecomendamos processar no máximo 50 por vez em máquinas fracas.\n\nTem certeza que deseja continuar?")) {
            startBtn.enabled = true;
            return;
        }
    }
    
    // OTIMIZAÇÕES MÁXIMAS DE PERFORMANCE PARA PC DE 8GB
    try {
        // Desabilita completamente o redraw e preview
        app.redraw();
        app.coordinateSystem = CoordinateSystem.ARTBOARDCOORDINATESYSTEM;
        
        // Força garbage collection antes de começar
        $.gc();
        
        // Desabilita preview em tempo real se possível
        try {
            app.preferences.setBooleanPreference("ShowRealTimeDrawing", false);
        } catch (prefError) {}
        
    } catch (perfError) {
        // Ignora erros de otimização
    }
    
    function processBatch() {
        // Verificação de timeout para evitar travamento
        var currentTime = new Date().getTime();
        if (currentTime - processStartTime > maxProcessingTime) {
            progressText.text = 'Timeout detectado - Processamento longo em andamento...';
            
            // Confirmação antes de cancelar
            var continueProcessing = confirm("O processamento está executando há mais de 10 minutos.\n\nProcessando objeto " + (i+1) + " de " + total + ".\n\nDeseja continuar processando? (Clique 'Cancelar' para interromper)");
            
            if (continueProcessing) {
                // Usuário quer continuar - estende o timeout por mais 10 minutos
                processStartTime = new Date().getTime();
                progressText.text = 'Continuando processamento... (' + (i+1) + '/' + total + ')';
            } else {
                // Usuário quer cancelar
                progressText.text = 'Processamento cancelado pelo usuário após timeout.';
                startBtn.enabled = true;
                cancelBtn.enabled = false;
                try {
                    app.redraw();
                    app.preferences.setBooleanPreference("ShowRealTimeDrawing", true);
                } catch (restoreError) {}
                alert("Processamento cancelado após 10+ minutos.\n\nForam processados " + i + " de " + total + " objetos.");
                return;
            }
        }
        
        if (cancelRequested) {
            progressText.text = 'Processamento cancelado.';
            startBtn.enabled = true;
            cancelBtn.enabled = false;
            // Reabilita redraw e restaura configurações
            try {
                app.redraw();
                app.preferences.setBooleanPreference("ShowRealTimeDrawing", true);
            } catch (restoreError) {}
            return;
        }
        
        // Lotes menores para PCs fracos (2 objetos por vez - ULTRA CONSERVADOR)
        var actualBatchSize = Math.min(batchSize, 2);
        var batchEnd = Math.min(i + actualBatchSize, total);
        
        for (; i < batchEnd; i++) {
            try {
                // Verificação de segurança - objeto ainda existe?
                if (!sel[i] || sel[i] === null) {
                    progressText.text = 'Objeto ' + (i+1) + ' não encontrado. Pulando...';
                    continue;
                }
                
                // Força garbage collection a cada objeto (MÁXIMA FREQUÊNCIA)
                $.gc(); $.gc();
                
                // Pausa maior para dar mais respiro ao sistema
                $.sleep(50);
                
                // Limpa toda a seleção primeiro
                try {
                    app.activeDocument.selection = null;
                } catch (selError) {
                    // Se não conseguir limpar seleção, pula este objeto
                    continue;
                }
                
                // Seleciona apenas o objeto atual com verificação
                try {
                    sel[i].selected = true;
                } catch (selectError) {
                    // Se não conseguir selecionar, pula este objeto
                    continue;
                }
                
                // Coleta dados ANTES (estrutura mínima)
                var objectData = {
                    index: i+1,
                    originalText: ""
                };
                
                try {
                    if (sel[i] && sel[i].typename === "TextFrame" && sel[i].contents) {
                        var textContent = String(sel[i].contents);
                        // Limita tamanho do texto para economizar memória
                        if (textContent.length > 300) {
                            textContent = textContent.substring(0, 300) + "...";
                        }
                        objectData.originalText = textContent;
                    }
                } catch (textError) {
                    objectData.originalText = "";
                }
                
                // Aplica a ação com timeout maior
                try {
                    app.doScript(actionNameField.text, actionSetField.text);
                } catch (actionError) {
                    objectData.originalText = "Erro na ação: " + actionError;
                }
                
                $.sleep(100); // Pausa muito maior após ação
                
                // Coleta dados APÓS (estrutura mínima)
                var postObjectData = {
                    currentText: ""
                };
                
                try {
                    if (sel[i].typename === "TextFrame" && sel[i].contents) {
                        var postTextContent = String(sel[i].contents);
                        // Limita tamanho do texto
                        if (postTextContent.length > 300) {
                            postTextContent = postTextContent.substring(0, 300) + "...";
                        }
                        postObjectData.currentText = postTextContent;
                    }
                } catch (textError) {
                    postObjectData.currentText = "";
                }
                
                // Armazena os dados (estrutura ultra-simplificada)
                variablesData.push({
                    index: i+1,
                    preData: objectData,
                    postData: postObjectData
                });
                
                // Limpa a seleção novamente
                app.activeDocument.selection = null;
                
            } catch (e) {
                try { app.activeDocument.selection = null; } catch (clearError) {}
                // Estrutura de erro simplificada
                variablesData.push({
                    index: i+1,
                    preData: { index: i+1, originalText: "Erro: " + e },
                    postData: { currentText: "" }
                });
            }
            updateProgress(i + 1, total);
        }
        
        if (i < total) {
            // Pausa muito longa entre lotes para dar "respiro" máximo ao sistema
            progressText.text = 'Pausando entre lotes... (' + i + '/' + total + ')';
            $.sleep(500); // Pausa muito maior
            
            // Força garbage collection múltipla entre lotes
            $.gc(); $.gc(); $.gc();
            
            // Pausa adicional para sistemas ultra-fracos
            $.sleep(200);
            
            // Força redraw para mostrar que não travou
            app.redraw();
            
            // Continua processamento
            processBatch();
        } else {
            progressText.text = 'Processamento concluído!';
            startBtn.enabled = true;
            cancelBtn.enabled = false;
            
            // Reabilita redraw e configurações no final
            try {
                app.redraw();
                app.preferences.setBooleanPreference("ShowRealTimeDrawing", true);
                $.gc(); // Limpeza final de memória
            } catch (restoreError) {}
            
            // Pergunta se deseja exportar CSV
            var exportCSV = confirm("Processamento concluído! Ação '" + actionNameField.text + "' executada para " + total + " objetos.\n\nDeseja exportar um arquivo CSV com os dados das variáveis?");
            if (exportCSV && variablesData.length > 0) {
                exportVariablesToCSVSafe(variablesData, variablePrefixField.text);
            } else if (!exportCSV) {
                alert("Processamento concluído sem exportação de CSV.");
            } else {
                alert("Nenhum dado de variável foi coletado para exportação.");
            }
        }
    }
    processBatch();
}

// Botão cancelar
cancelBtn.onClick = function() {
    cancelRequested = true;
    cancelBtn.enabled = false;
    startBtn.enabled = true;
    progressText.text = 'Cancelamento solicitado...';
};

// Função para exportar variáveis já existentes no documento - SUPER OTIMIZADA PARA MÁQUINAS FRACAS
function exportExistingVariables() {
    try {
        // Múltiplas limpezas de memória aggressivas
        $.gc(); $.gc(); $.gc();
        
        if (app.documents.length === 0) {
            alert('Nenhum documento aberto.');
            return;
        }
        
        var doc = app.activeDocument;
        var variables = doc.variables;
        
        if (variables.length === 0) {
            alert('Nenhuma variável encontrada no documento atual.');
            return;
        }
        
        // Limite muito restritivo para máquinas fracas
        if (variables.length > 25) {
            if (!confirm("Você tem " + variables.length + " variáveis. Para máquinas fracas, o limite recomendado é 25.\n\nProcessar todas pode causar travamento. Continuar?")) {
                return;
            }
        }
        
        // Processa em micro-lotes para evitar crash
        var variablesData = [];
        var maxVariables = Math.min(variables.length, 30); // Limite ultra-baixo
        var processed = 0;
        
        // Processamento em chunks de 5 variáveis
        for (var chunk = 0; chunk < Math.ceil(maxVariables / 5); chunk++) {
            var startIdx = chunk * 5;
            var endIdx = Math.min(startIdx + 5, maxVariables);
            
            // Processa chunk atual
            for (var i = startIdx; i < endIdx; i++) {
                try {
                    var variable = variables[i];
                    if (variable && variable.name) {
                        // Estrutura mínima para economizar memória
                        var varName = String(variable.name);
                        variablesData.push({
                            index: processed + 1,
                            preData: { originalText: varName },
                            postData: { currentText: varName }
                        });
                        processed++;
                    }
                } catch (varError) {
                    // Falha silenciosa para não interromper
                    continue;
                }
            }
            
            // Limpeza agressiva entre chunks
            $.gc(); $.gc();
            $.sleep(50); // Pausa maior para dar respiro ao sistema
            
            // Feedback visual para chunks grandes
            if (maxVariables > 10) {
                app.redraw(); // Força redraw para mostrar que não travou
            }
        }
        
        if (variablesData.length === 0) {
            alert('Nenhuma variável válida encontrada para exportação.');
            return;
        }
        
        // Limpeza final brutal antes da exportação
        $.gc(); $.gc(); $.gc();
        $.sleep(100);
        
        exportVariablesToCSVSafe(variablesData, variablePrefixField.text);
        
    } catch (e) {
        alert('Erro ao exportar variáveis existentes: ' + e);
        // Limpeza de emergência
        try { $.gc(); $.gc(); $.gc(); } catch (gcError) {}
    }
}

// Botão exportar CSV existente - COM PROTEÇÃO EXTRA
exportBtn.onClick = function() {
    try {
        // Desabilita botão para evitar duplo clique
        exportBtn.enabled = false;
        exportBtn.text = 'Processando...';
        
        // Pausa para interface se atualizar
        $.sleep(100);
        app.redraw();
        
        exportExistingVariables();
        
    } catch (btnError) {
        alert('Erro no botão de exportação: ' + btnError);
    } finally {
        // Sempre reabilita o botão
        exportBtn.enabled = true;
        exportBtn.text = 'Exportar CSV Existente';
        app.redraw();
    }
};

// Botão start
startBtn.onClick = function() {
    if (app.documents.length === 0) {
        alert('Nenhum documento aberto.');
        return;
    }
    var sel = app.selection;
    if (!sel || sel.length === 0) {
        alert('Por favor, selecione alguns objetos primeiro.');
        return;
    }
    // Backup automático (apenas se ativado)
    if (backupCheckbox.value) {
        try {
            var doc = app.activeDocument;
            var originalPath = doc.fullName;
            var backupPath = originalPath.parent + "/" + originalPath.name.replace(/\.ai$/i, "-backup.ai");
            doc.saveAs(new File(backupPath));
            alert("Backup salvo em: " + backupPath);
        } catch (backupError) {
            alert("Não foi possível salvar o backup automático: " + backupError);
        }
    }
    startBtn.enabled = false;
    cancelBtn.enabled = true;
    cancelRequested = false;
    updateProgress(0, sel.length);
    
    // Força garbage collection antes de começar (MÚLTIPLAS VEZES)
    $.gc(); $.gc(); $.gc();
    
    // Lotes ultra-pequenos para máquinas fracas (2 ao invés de 5)
    processSelectionAsync(sel, 2);
};

// Mostrar interface
win.show();

// ===============================

// Função para coletar dados do objeto de forma segura
function collectObjectData(obj, index) {
    try {
        var data = {
            index: index,
            objectType: "Unknown",
            originalText: ""
        };
        
        // Coleta tipo do objeto de forma segura
        try {
            data.objectType = obj.typename || "Unknown";
        } catch (typeError) {
            data.objectType = "Error";
        }
        
        // Se for um texto, coleta o conteúdo
        try {
            if (data.objectType === "TextFrame" && obj.contents) {
                data.originalText = String(obj.contents);
            }
        } catch (textError) {
            data.originalText = "";
        }
        
        return data;
    } catch (e) {
        return {
            index: index,
            objectType: "Error",
            originalText: ""
        };
    }
}

// Função para coletar dados após o processamento
function collectPostObjectData(obj, index) {
    try {
        var data = {
            currentText: "",
            hasVariables: false
        };
        
        // Se for um texto, coleta o conteúdo atual
        try {
            if (obj.typename === "TextFrame" && obj.contents) {
                data.currentText = String(obj.contents);
            }
        } catch (textError) {
            data.currentText = "";
        }
        
        // Verifica se há variáveis no documento de forma simples
        try {
            var varCount = app.activeDocument.variables.length;
            data.hasVariables = varCount > 0;
            data.variableCount = varCount;
        } catch (varError) {
            data.hasVariables = false;
            data.variableCount = 0;
        }
        
        return data;
    } catch (e) {
        return {
            currentText: "",
            hasVariables: false
        };
    }
}

// Função para exportar dados para CSV no formato solicitado - VERSÃO SEGURA PARA MÁQUINAS FRACAS
function exportVariablesToCSVSafe(data, variablePrefix) {
    try {
        // Limpeza agressiva de memória antes de começar
        $.gc(); $.gc(); $.gc();
        
        // Solicita local para salvar o arquivo
        var saveFile = File.saveDialog("Salvar CSV de Variáveis", "*.csv");
        
        if (!saveFile) {
            return; // Usuário cancelou
        }
        
        // Processa em micro-lotes para evitar crash
        var totalItems = data.length;
        var processedItems = 0;
        var chunkSize = 5; // Processa apenas 5 itens por vez
        
        // Arrays temporários pequenos
        var csvLines = [];
        var variableNames = [];
        var variableContents = [];
        
        // Primeiro, cria apenas os nomes das variáveis (sem processar conteúdo)
        for (var nameIdx = 0; nameIdx < totalItems; nameIdx++) {
            variableNames.push('"' + variablePrefix + (nameIdx + 1) + '"');
            
            // Limpeza a cada 10 nomes
            if (nameIdx % 10 === 0) {
                $.gc();
            }
        }
        
        // Agora processa o conteúdo em chunks
        for (var chunk = 0; chunk < Math.ceil(totalItems / chunkSize); chunk++) {
            var startIdx = chunk * chunkSize;
            var endIdx = Math.min(startIdx + chunkSize, totalItems);
            
            // Processa chunk atual
            for (var i = startIdx; i < endIdx; i++) {
                var item = data[i];
                var content = "";
                
                try {
                    // Obtém conteúdo de forma mais segura
                    if (item && item.postData && item.postData.currentText) {
                        content = String(item.postData.currentText);
                    } else if (item && item.preData && item.preData.originalText) {
                        content = String(item.preData.originalText);
                    }
                    
                    // Formatação mais simples e rápida para CSV
                    variableContents.push(formatForCSVSimple(content));
                    
                } catch (contentError) {
                    // Em caso de erro, adiciona campo vazio
                    variableContents.push('""');
                }
            }
            
            // Limpeza agressiva entre chunks
            $.gc(); $.gc();
            $.sleep(30);
        }
        
        // Escreve arquivo de forma mais segura
        try {
            saveFile.encoding = "UTF-8";
            saveFile.lineFeed = "Unix";
            saveFile.open("w");
            
            // Escreve BOM UTF-8
            saveFile.write("\uFEFF");
            
            // Escreve cabeçalho
            saveFile.writeln(variableNames.join(","));
            
            // Escreve conteúdo
            saveFile.writeln(variableContents.join(","));
            
            saveFile.close();
            
            // Limpeza final
            $.gc(); $.gc();
            
            alert("Arquivo CSV exportado com sucesso!\nLocal: " + saveFile.fsName + "\n\nForam processadas " + totalItems + " variáveis.");
            
        } catch (writeError) {
            alert("Erro ao escrever arquivo CSV: " + writeError);
        }
        
    } catch (e) {
        alert("Erro ao exportar CSV: " + e);
        // Limpeza de emergência
        try { $.gc(); $.gc(); $.gc(); } catch (gcError) {}
    }
}

// Função de formatação CSV simplificada para economizar memória
function formatForCSVSimple(text) {
    if (!text) return '""';
    
    try {
        // Converte para string de forma segura
        text = String(text);
        
        // Limite de tamanho para evitar travamento (máximo 500 caracteres)
        if (text.length > 500) {
            text = text.substring(0, 500) + "...";
        }
        
        // PRESERVA quebras de linha (versão otimizada)
        text = text.replace(/\r\n/g, "\\n").replace(/\r/g, "\\n").replace(/\n/g, "\\n");
        
        // Limpeza básica
        text = text.replace(/\t/g, " ").replace(/ +/g, " ").replace(/^ +| +$/gm, "");
        
        // Escapa aspas
        text = text.replace(/"/g, '""');
        
        return '"' + text + '"';
    } catch (formatError) {
        return '""';
    }
}
