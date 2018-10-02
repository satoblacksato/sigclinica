
export const cargarPacientesAsync = (context) => {
	context.commit('cargarPacientes');
}

export const paginaSiguienteAsync = (context) => {
	context.commit('paginaSiguiente');
}

export const paginaAtrasAsync = (context) => {
	context.commit('paginaAtras');
}

export const buscarAsync = (context, buscar) => {
	context.commit('buscar', buscar)
}
