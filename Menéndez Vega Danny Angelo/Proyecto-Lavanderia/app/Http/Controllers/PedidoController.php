<?php

namespace App\Http\Controllers;

use App\Models\Pedido;
use App\Models\PedidoServicio;
use Illuminate\Http\Request;

class PedidoController extends Controller
{

    public function index()
    {
        $pedidos = Pedido::with(['metodoPago','pedidoServicios'])->get();
        return response()->json($pedidos);
    }

    public function store(Request $request)
    {
            $request->validate([
                'id_cliente' => 'required|exists:clientes,id_cliente',
                'id_metodo_pago' => 'required|exists:metodo_pago,id_metodo_pago',
                'cantidad_pedido' => 'required|numeric',
                'array_servicios' => 'required|array',
                'array_servicios*.id_tipo_servicio' => 'required|exists:tipo_servicio,id_tipo_servicio',
                'fecha_pedido' => 'required|date',
                'array_servicios*.cantidad_servicio' => 'required|numeric',
                'array_servicios*.descripcion' => 'required',
                'observacion' => 'required',

            ],[
                'id_cliente.required' => 'El cliente es requerido',
                'id_metodo_pago.required' => 'El método de pago es requerido',
                'cantidad_pedido.required' => 'La cantidad de pedido es requerida',
                'array_servicios.required' => 'Los servicios son requeridos',
                'array_servicios.array' => 'Los servicios deben ser un arreglo',
                'array_servicios*.id_tipo_servicio.required' => 'El tipo de servicio es requerido',
                'array_servicios*.id_tipo_servicio.exists' => 'El tipo de servicio no existe',
                'fecha_pedido.required' => 'La fecha del pedido es requerida',
                'array_servicios*.cantidad_servicio.required' => 'La cantidad de servicio es requerida',
                'array_servicios*.cantidad_servicio.numeric' => 'La cantidad de servicio debe ser numérica',
                'array_servicios*.descripcion.required' => 'La descripción del servicio es requerida',
            ]);
            $servicios = $request->array_servicios;
            $pedido = new Pedido();
            $pedido->id_cliente = $request->id_cliente;
            $pedido->id_metodo_pago = $request->id_metodo_pago;
            $pedido->cantidad_pedido = $request->cantidad_pedido;
            $pedido->observacion = $request->observacion;
            $pedido->fecha_pedido = $request->fecha_pedido;
            $pedido->save();

            foreach($servicios as $servicio){
                $pedido_servicio = new PedidoServicio();
                $pedido_servicio->id_pedido = $pedido->id_pedido;
                $pedido_servicio->id_tipo_servicio = $servicio['id_tipo_servicio'];
                $pedido_servicio->cantidad_servicio = $servicio['cantidad_servicio'];
                $pedido_servicio->descripcion = $servicio['descripcion'];
                $pedido_servicio->save();
            }

            $pedido->save();
            return response()->json($pedido);

    }

    public function show($id)
    {
        $pedido = Pedido::with('metodoPago')->find($id);
        return response()->json($pedido);
    }

    public function update(Request $request, $id)
    {
        $request->validate([
            'id_cliente' => 'required|exists:clientes,id_cliente',
            'id_metodo_pago' => 'required|exists:metodo_pago,id_metodo_pago',
            'cantidad_pedido' => 'required|numeric',
        ]);
        $pedido = Pedido::find($id);
        $pedido->update($request->all());
        return response()->json($pedido);
    }

    public function destroy($id)
    {
        $pedido = Pedido::find($id);
        $pedido->update(['estado' => false]);
        return response()->json(['message' => 'Pedido ']);
    }
}
