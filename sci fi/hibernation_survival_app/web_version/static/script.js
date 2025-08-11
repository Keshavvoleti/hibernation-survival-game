function updateStatus(data) {
    document.getElementById('health').textContent = data.health;
    document.getElementById('hand-status').textContent = data.hand_intact ? 'Intact' : 'Missing';
    document.getElementById('hibernation-status').textContent = data.is_hibernating ? 'Hibernating' : 'Awake';
    
    if (data.health < 30) {
        document.getElementById('health').classList.add('critical');
    } else {
        document.getElementById('health').classList.remove('critical');
    }
    
    if (data.dead) {
        document.querySelectorAll('button').forEach(btn => {
            if (btn.textContent !== '🔄 Reset') btn.disabled = true;
        });
    }
}

function showMessage(msg) {
    const messageBox = document.getElementById('message');
    messageBox.textContent = msg;
    messageBox.classList.add('active');
    setTimeout(() => messageBox.classList.remove('active'), 3000);
}

async function cutHand() {
    try {
        const response = await fetch('/cut_hand', { method: 'POST' });
        const data = await response.json();
        if (data.error) {
            showMessage(data.error);
        } else {
            showMessage(data.message);
            updateStatus(data);
        }
    } catch (error) {
        showMessage('Failed to amputate hand');
    }
}

async function cutWithKnife() {
    try {
        const response = await fetch('/cut_with_knife', { method: 'POST' });
        const data = await response.json();
        if (data.error) {
            showMessage(data.error);
        } else {
            showMessage(data.message + " (Fatal when waking)");
            updateStatus(data);
        }
    } catch (error) {
        showMessage('Failed to make small cut');
    }
}

async function giveMeds() {
    try {
        const response = await fetch('/give_meds', { method: 'POST' });
        const data = await response.json();
        showMessage(data.message);
        updateStatus(data);
    } catch (error) {
        showMessage('Failed to administer meds');
    }
}

async function wakeUp() {
    try {
        const response = await fetch('/wake_up', { method: 'POST' });
        const data = await response.json();
        showMessage(data.message);
        updateStatus(data);
    } catch (error) {
        showMessage('Failed to wake subject');
    }
}

async function resetExperiment() {
    try {
        const response = await fetch('/reset', { method: 'POST' });
        const data = await response.json();
        showMessage(data.message);
        updateStatus(data);
        document.querySelectorAll('button').forEach(btn => btn.disabled = false);
    } catch (error) {
        showMessage('Failed to reset experiment');
    }
}