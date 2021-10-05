async function handleIt(){
    clearList()
    let nivel = parseInt(document.getElementById('nivel').value, 10)
    let nivel0 = nivel
    let xp_atual = parseInt(document.getElementById('xp-atual').value, 10)
    let add_xp = parseInt(document.getElementById('add-xp').value, 10)
    let xp_needed = nivel * 100 - xp_atual

    while (xp_needed < add_xp){
        add_xp -= xp_needed
        nivel += 1
        xp_needed = nivel * 100
    }
    xp_atual = add_xp
    add_xp = 0
    if (xp_atual == xp_needed){
        nivel += 1
        xp_atual = 0
    }

    if (nivel0 == nivel)
        return
        
    let upgrades = {
        att_points: 0,
        common_points: 0,
        superior_points: 0,
        divine_points: 0,
        bonus_points: {
            str: 0,
            dex: 0,
            int: 0,
            cha: 0,
            con: 0
        },
        return_points: 0
    }
    
    let scaling;
    await getScaling(nivel0 + 1, nivel).then(data => {scaling = data['result']})

    for ( let n = nivel0 + 1; n <= nivel; n++){
        let scale = scaling[n]

        upgrades.att_points += scale.att_points
        upgrades.common_points += scale.common_points
        upgrades.superior_points += scale.superior_points
        upgrades.divine_points += scale.divine_points
        addBonus(upgrades.bonus_points, scale.bonus_points)
        upgrades.return_points += scale.return_points
    }

    buildList(upgrades, nivel, xp_atual)
}

function clearList(){
    let ul = document.getElementById('lista_bonus')
    ul.innerHTML = ''
}

function buildList(upgrades, nivel, xp_atual){
    var items = [
        'Novo nivel: ' + nivel + ' XP Sobrando: ' + xp_atual,
        'Você ganhou:',
        upgrades.att_points + ' pontos de atributo',
        upgrades.common_points + ' pontos comuns',
        upgrades.superior_points + ' pontos superiores',
        upgrades.divine_points + ' pontos divinos',
        upgrades.return_points + ' pontos de retorno'
    ]

    for (var key in upgrades.bonus_points){
        value = upgrades.bonus_points[key]
        if (value != 0 && !isNaN(value)) {
            items.push('+' + value + ' ' + key)
        }
    }

    ul = document.getElementById('lista_bonus')
    ul.innerHTML = ''

    for (var i in items){
        var li = document.createElement('li')
        ul.appendChild(li)
        li.innerHTML = li.innerHTML + items[i]
    }
}

function addBonus(attributes, bonus){
    if (bonus == '0')
        return

    var split = bonus.split('_')

    if (split[1] == 'ALL'){
        for (var key in attributes)
            attributes[key] += parseInt(split[0], 10)
    }

    which_att = split[1].toLowerCase()
    attributes[which_att] += parseInt(split[0])
}

const scaling_url = window.location.origin + '/api/scaling'

async function getScaling(start, end){
    let params = '?start=' + start + '&end=' + end
    return await fetch(scaling_url + params)
    .then(r => r.json())
}