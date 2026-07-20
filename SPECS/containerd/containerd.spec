# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name                   containerd
%define go_import_path          github.com/containerd/containerd
%define containerd_version      1.7.28
%define commit_id               b98a3aace656320842a23f4a392a33f46af97866
# containerd v1.7.28/go.mod requires github.com/containerd/containerd/api
# v1.8.0. The API source uses the separate api/v1.8.0 tag.
%define api_import_path         github.com/containerd/containerd/api
%define api_version             1.8.0
%define api_dir                 containerd-api-v%{api_version}
%define containerd_buildtags    no_cri no_tracing no_aufs no_btrfs no_devmapper no_zfs

Name:           containerd
Version:        %{containerd_version}
Release:        %autorelease
Summary:        Open and reliable container runtime
License:        Apache-2.0
URL:            https://github.com/containerd/containerd
#!RemoteAsset:  sha256:546aa9fdb04a0cd40a5cbc5c931c269d42522d473abd7234b98d98e63316ed9b
Source0:        https://github.com/containerd/containerd/archive/refs/tags/v%{containerd_version}.tar.gz#/%{_name}-%{containerd_version}.tar.gz
#!RemoteAsset:  sha256:7142bc4eafa2418964aa56c89f3d0d507cb658c141524ea6bab566c109f311e8
Source1:        https://github.com/containerd/containerd/archive/refs/tags/api/v%{api_version}.tar.gz#/%{_name}-api-%{api_version}.tar.gz
BuildSystem:    golang

# runtime-spec 1.3 changed LinuxPids.Limit to *int64.
Patch2000:      2000-adapt-to-runtime-spec-1.3.patch

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  make
BuildRequires:  systemd-rpm-macros
BuildRequires:  go(dario.cat/mergo)
BuildRequires:  go(github.com/Microsoft/hcsshim)
BuildRequires:  go(github.com/beorn7/perks)
BuildRequires:  go(github.com/cespare/xxhash/v2)
BuildRequires:  go(github.com/cilium/ebpf)
BuildRequires:  go(github.com/containerd/cgroups)
BuildRequires:  go(github.com/containerd/cgroups/v3)
BuildRequires:  go(github.com/containerd/console)
BuildRequires:  go(github.com/containerd/continuity)
BuildRequires:  go(github.com/containerd/errdefs)
BuildRequires:  go(github.com/containerd/fifo)
BuildRequires:  go(github.com/containerd/go-cni)
BuildRequires:  go(github.com/containerd/go-runc)
BuildRequires:  go(github.com/containerd/log)
BuildRequires:  go(github.com/containerd/platforms)
BuildRequires:  go(github.com/containerd/ttrpc)
BuildRequires:  go(github.com/containerd/typeurl/v2)
BuildRequires:  go(github.com/coreos/go-systemd/v22)
BuildRequires:  go(github.com/containernetworking/cni)
BuildRequires:  go(github.com/cpuguy83/go-md2man/v2)
BuildRequires:  go(github.com/distribution/reference)
BuildRequires:  go(github.com/docker/go-events)
BuildRequires:  go(github.com/docker/go-metrics)
BuildRequires:  go(github.com/docker/go-units)
BuildRequires:  go(github.com/felixge/httpsnoop)
BuildRequires:  go(github.com/go-logr/logr)
BuildRequires:  go(github.com/go-logr/stdr)
BuildRequires:  go(github.com/godbus/dbus/v5)
BuildRequires:  go(github.com/gogo/protobuf)
BuildRequires:  go(github.com/golang/protobuf)
BuildRequires:  go(github.com/google/go-cmp)
BuildRequires:  go(github.com/google/uuid)
BuildRequires:  go(github.com/grpc-ecosystem/go-grpc-middleware)
BuildRequires:  go(github.com/grpc-ecosystem/go-grpc-prometheus)
BuildRequires:  go(github.com/intel/goresctrl)
BuildRequires:  go(github.com/klauspost/compress)
BuildRequires:  go(github.com/klauspost/cpuid/v2)
BuildRequires:  go(github.com/matttproud/golang_protobuf_extensions)
BuildRequires:  go(github.com/minio/sha256-simd)
BuildRequires:  go(github.com/moby/locker)
BuildRequires:  go(github.com/moby/sys/mountinfo)
BuildRequires:  go(github.com/moby/sys/signal)
BuildRequires:  go(github.com/moby/sys/user)
BuildRequires:  go(github.com/moby/sys/userns)
BuildRequires:  go(github.com/opencontainers/go-digest)
BuildRequires:  go(github.com/opencontainers/image-spec)
BuildRequires:  go(github.com/opencontainers/runtime-spec)
BuildRequires:  go(github.com/opencontainers/selinux)
BuildRequires:  go(github.com/pelletier/go-toml)
BuildRequires:  go(github.com/pkg/errors)
BuildRequires:  go(github.com/prometheus/client_golang)
BuildRequires:  go(github.com/prometheus/client_model)
BuildRequires:  go(github.com/prometheus/common)
BuildRequires:  go(github.com/prometheus/procfs)
BuildRequires:  go(github.com/russross/blackfriday/v2)
BuildRequires:  go(github.com/sirupsen/logrus)
BuildRequires:  go(github.com/urfave/cli)
BuildRequires:  go(go.etcd.io/bbolt)
BuildRequires:  go(go.opentelemetry.io/auto/sdk)
BuildRequires:  go(go.opentelemetry.io/contrib/instrumentation/google.golang.org/grpc/otelgrpc)
BuildRequires:  go(go.opentelemetry.io/contrib/instrumentation/net/http/otelhttp)
BuildRequires:  go(go.opentelemetry.io/otel)
BuildRequires:  go(go.opentelemetry.io/otel/metric)
BuildRequires:  go(go.opentelemetry.io/otel/trace)
BuildRequires:  go(golang.org/x/net)
BuildRequires:  go(golang.org/x/sync)
BuildRequires:  go(golang.org/x/sys)
BuildRequires:  go(golang.org/x/text)
BuildRequires:  go(google.golang.org/genproto)
BuildRequires:  go(google.golang.org/genproto/googleapis/rpc)
BuildRequires:  go(google.golang.org/grpc)
BuildRequires:  go(google.golang.org/protobuf)
BuildRequires:  go(gopkg.in/inf.v0)
BuildRequires:  go(gopkg.in/yaml.v2)
BuildRequires:  go(k8s.io/apimachinery)
BuildRequires:  go(sigs.k8s.io/yaml)

Requires:       runc

%description
containerd is an industry-standard container runtime with an emphasis on
simplicity, robustness, and portability. This package provides the daemon,
administration client, and runc shims. Kubernetes CRI, tracing, optional
snapshotters, and NRI are disabled.

%package     -n go-github-containerd-containerd-api
Version:        %{api_version}
Summary:        Go API definitions for containerd
BuildArch:      noarch
Provides:       go(%{api_import_path}) = %{api_version}

Requires:       go(github.com/containerd/ttrpc)
Requires:       go(github.com/containerd/typeurl/v2)
Requires:       go(github.com/opencontainers/go-digest)
Requires:       go(github.com/opencontainers/image-spec)
Requires:       go(google.golang.org/genproto)
Requires:       go(google.golang.org/genproto/googleapis/rpc)
Requires:       go(google.golang.org/grpc)
Requires:       go(google.golang.org/protobuf)

%description -n go-github-containerd-containerd-api
This package provides the independently versioned API definitions used by
containerd clients and services.

%prep -a
# The program tag does not include the API submodule source. Add the independently
# tagged API tree to the same GOPATH checkout before building containerd.
tar -xzf %{SOURCE1}
cp %{api_dir}/LICENSE %{api_dir}/api/LICENSE
rm -rf %{_builddir}/go/src/%{go_import_path}/api
cp -a %{api_dir}/api %{_builddir}/go/src/%{go_import_path}/api
# Use distribution Go modules instead of the vendored copies.
rm -rf %{_builddir}/go/src/%{go_import_path}/{vendor,api/vendor}
pushd %{_builddir}/go/src/%{go_import_path}
sed -i 's|/usr/local/bin/containerd|%{_bindir}/containerd|' containerd.service
# Docker does not use the optional NRI integration; omitting it keeps the
# dependency closure limited to the daemon and runc shims.
sed -i '\#github.com/containerd/containerd/pkg/nri/plugin#d' cmd/containerd/builtins/builtins.go
popd

%build
%go_common
cd %{_builddir}/go/src/%{go_import_path}
export CGO_ENABLED=1
export GOTOOLCHAIN=local
# containerd-stress pulls in CRI integration packages that are not shipped here.
# Keep the upstream target, but limit it to the runtime binaries installed below.
%{__make} VERSION=v%{containerd_version} REVISION=%{commit_id} \
    BUILDTAGS="%{containerd_buildtags}" \
    COMMANDS="ctr containerd containerd-shim containerd-shim-runc-v1 containerd-shim-runc-v2" \
    binaries

%install
cd %{_builddir}/go/src/%{go_import_path}
install -D -m 0755 bin/ctr %{buildroot}%{_bindir}/ctr
install -D -m 0755 bin/containerd %{buildroot}%{_bindir}/containerd
install -D -m 0755 bin/containerd-shim %{buildroot}%{_bindir}/containerd-shim
install -D -m 0755 bin/containerd-shim-runc-v1 %{buildroot}%{_bindir}/containerd-shim-runc-v1
install -D -m 0755 bin/containerd-shim-runc-v2 %{buildroot}%{_bindir}/containerd-shim-runc-v2
install -D -m 0644 containerd.service %{buildroot}%{_unitdir}/containerd.service
install -d %{buildroot}%{go_sys_gopath}/github.com/containerd/containerd
cp -a api %{buildroot}%{go_sys_gopath}/github.com/containerd/containerd/api

%check
%{buildroot}%{_bindir}/ctr --version
%{buildroot}%{_bindir}/containerd --version
%{buildroot}%{_bindir}/containerd-shim -v
%{buildroot}%{_bindir}/containerd-shim-runc-v1 -v
%{buildroot}%{_bindir}/containerd-shim-runc-v2 -v
%go_common
cd %{_builddir}/go/src/%{go_import_path}
export CGO_ENABLED=1
export GOTOOLCHAIN=local
# Run the tests for the shipped commands and API source module.
go test -vet=off -tags "%{containerd_buildtags}" \
    ./cmd/ctr ./cmd/containerd ./cmd/containerd-shim \
    ./cmd/containerd-shim-runc-v1 ./cmd/containerd-shim-runc-v2 ./api/...

%post
%systemd_post containerd.service

%preun
%systemd_preun containerd.service

%postun
%systemd_postun_with_restart containerd.service

%files
%doc README.md
%license LICENSE NOTICE
%{_bindir}/ctr
%{_bindir}/containerd
%{_bindir}/containerd-shim
%{_bindir}/containerd-shim-runc-v1
%{_bindir}/containerd-shim-runc-v2
%{_unitdir}/containerd.service

%files -n go-github-containerd-containerd-api
%doc %{api_dir}/api/README.md
%license %{api_dir}/api/LICENSE
%{go_sys_gopath}/%{api_import_path}

%changelog
%autochangelog
