import { createRootRouteWithContext, Outlet } from "@tanstack/react-router";
import Navbar from "../components/Navbar";
import { ReactQueryDevtools } from "@tanstack/react-query-devtools";
import { QueryClient } from "@tanstack/react-query";
import { lazy } from "react";

const TanStackRouterDevtools =
  process.env.NODE_ENV === "production"
    ? () => null
    : lazy(() =>
        import("@tanstack/router-devtools").then((module) => ({
          default: module.TanStackRouterDevtools,
        })),
      );

export const Route = createRootRouteWithContext<{
  queryClient: QueryClient;
}>()({
  component: () => (
    <>
      <div className="container mx-auto grid min-h-screen grid-rows-[auto_1fr] gap-4 p-4 ">
        <header className="sticky top-4">
          <Navbar />
        </header>
        <main>
          <Outlet />
        </main>
      </div>
      <ReactQueryDevtools />
      <TanStackRouterDevtools />
    </>
  ),
});
